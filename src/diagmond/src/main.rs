pub mod logging;
pub mod system {
    // pub mod mm_dbus_lock;
    pub mod mm_udev_lock;
    pub mod serial_devices;
    pub mod udev_rules;
    pub mod usb_devices;
}
pub mod dbus {
    pub mod device;
    pub mod manager;
}

use crate::dbus::manager::{Diagmond, DiagmondSignals};
use crate::logging::Logging;
use crate::system::serial_devices::list_devices;
use crate::system::usb_devices::{UsbDevicesEndpointResp, get_usb_metadata};

#[cfg(target_os = "linux")]
use std::os::unix::process::CommandExt;

use futures_util::StreamExt;
use tokio_serial::SerialPortInfo;
use zbus::connection::Builder;

#[tokio::main]
async fn main() -> zbus::Result<()> {
    // Set up logging
    Logging::setup_logging_main_proc();

    #[cfg(target_os = "linux")]
    if nix::unistd::geteuid().as_raw() != 0 {
        let args: Vec<String> = std::env::args().collect();
        let _ = std::process::Command::new("pkexec").args(args).exec();
        log::error!("Could not launch pkexec");
        std::process::exit(1);
    }

    let udev_rules = crate::system::udev_rules::get_udev_rules_data().await?;

    let diagmond = Diagmond {
        usb_data: "null".to_string(),
        udev_rules: serde_json::to_string_pretty(&udev_rules).unwrap(), // WIP
        tokio_serial_data: "null".to_string(),
        devices: vec![],
    };

    let connection = Builder::system()?
        .name("com.p1security.diagmond")?
        .serve_at("/com/p1security/diagmond", diagmond)?
        .build()
        .await?;

    // Spawn inotify watch over /run/udev/rules.d
    tokio::spawn(crate::system::udev_rules::watch_udev_rules(
        connection.clone(),
    ));

    // Spawn USB parsing code and retrieve JSON serialized
    // contents + send it back through D-Bus when we have connections
    let mut hotplug_watch = nusb::watch_devices().unwrap();

    loop {
        let usb_devices: UsbDevicesEndpointResp = get_usb_metadata().await;

        let devices_resp_string = serde_json::to_string_pretty(&usb_devices).unwrap();
        log::info!("USB devices list received");

        let serial_devices: Vec<SerialPortInfo> = list_devices();

        let serial_devices_string = serde_json::to_string_pretty(&serial_devices).unwrap();
        log::info!("Serial devices list received");

        // Trigger the DBus property change
        {
            let iface_ref = connection
                .object_server()
                .interface::<_, Diagmond>("/com/p1security/diagmond")
                .await?;

            let mut iface = iface_ref.get_mut().await;
            iface.usb_data = devices_resp_string.clone();
            iface.tokio_serial_data = serial_devices_string.clone();

            // Send the DBus-serialized JSON data to the Python
            // process (and eventually display it to the UI)

            iface_ref.usb_data_updated(&devices_resp_string).await?;
            iface_ref
                .tokio_serial_data_updated(&serial_devices_string)
                .await?;
        }

        let next_event = hotplug_watch.next().await.unwrap();
        log::info!("USB event received: {:?}", next_event);
    }
}
