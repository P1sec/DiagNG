use inotify::{Inotify, StreamExt, WatchMask};

use crate::dbus::manager::{Diagmond, DiagmondSignals};
use crate::system::mm_udev_lock::reload_udev_rules;

const UDEV_RULES_DIR: &'static str = "/run/udev/rules.d";

// Use "serde_json" to encode an array of UDevRule
// objects to a string (+ the inotify Rust module)
//
// See: https://github.com/hannobraun/inotify-rs
//     => https://github.com/hannobraun/inotify-rs/blob/main/examples/stream.rs
//
// [
//     {
//         "rule_file_name": "",
//         "rule_text": ""
//     },
//     ....
// ]

#[derive(serde::Serialize, serde::Deserialize)]
struct UDevRule {
    rule_file_name: String,
    rule_text: String,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UDevRuleList(Vec<UDevRule>);

pub async fn get_udev_rules_data(stale_rules: bool) -> zbus::Result<UDevRuleList> {
    let mut rules_vec: Vec<UDevRule> = vec![];

    let mut removed_rules = false;

    std::fs::create_dir_all(UDEV_RULES_DIR)?;

    for entry in std::fs::read_dir(UDEV_RULES_DIR)? {
        let entry = entry?;
        let path = entry.path();

        let base_name = path.file_name().unwrap().display().to_string();
        let full_name = path.display().to_string();

        if stale_rules && base_name.starts_with("99-diagmond-blacklist-") {
            log::warn!("Removing stale rule: {}", full_name);
            std::fs::remove_file(&path)?;
            removed_rules = true;
        } else if let Ok(content) = std::fs::read_to_string(&path) {
            rules_vec.push(UDevRule {
                rule_file_name: full_name,
                rule_text: content,
            });
        }
    }

    if removed_rules {
        reload_udev_rules(None).await?;
    }

    Ok(UDevRuleList(rules_vec))
}

pub async fn watch_udev_rules(connection: zbus::Connection) -> zbus::Result<()> {
    let inotify = Inotify::init()?;

    inotify.watches().add(
        UDEV_RULES_DIR,
        WatchMask::CREATE
            | WatchMask::DELETE
            | WatchMask::CLOSE_WRITE
            | WatchMask::MODIFY
            | WatchMask::MOVED_FROM
            | WatchMask::MOVED_TO,
    )?;

    let mut buffer = [0; 1024];
    let mut stream = inotify.into_event_stream(&mut buffer)?;

    while let Some(event_or_error) = stream.next().await {
        log::debug!("Received inotify event: {:?}", event_or_error?);

        let udev_rules = get_udev_rules_data(false).await?;
        let udev_rules = serde_json::to_string_pretty(&udev_rules).unwrap();

        // Send ZBus upstream update:

        // Trigger the DBus property change
        {
            let iface_ref = connection
                .object_server()
                .interface::<_, Diagmond>("/com/p1security/diagmond")
                .await?;

            let mut iface = iface_ref.get_mut().await;
            iface.udev_rules = udev_rules.clone();

            // Send the DBus-serialized JSON data to the Python
            // process (and eventually display it to the UI)

            iface_ref.udev_rules_updated(&udev_rules).await?;
        }
    }

    Ok(())
}
