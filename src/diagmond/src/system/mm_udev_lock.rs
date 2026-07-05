use std::io::Write;
use tokio::process::Command;

// Implemented based off QCSuper logic
// See: https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/usb_modem_pyserial.py

pub async fn reload_udev_rules(device_name: Option<&str>) -> zbus::Result<()> {
    // MANPAGE TO READ: https://man7.org/linux/man-pages/man7/udev.7.html

    // WIP: Sync code contained in "udev_rules_dir.py"

    // Reload udev rules
    //    => udevadm + https://docs.rs/tokio/latest/tokio/process/index.html ?

    // If using CLI:
    //  - "udevadm control --reload-rules"
    //  - "udevadm trigger --name-match=%s" % full_name
    // If using another channel: ?

    let mut child = Command::new("udevadm")
        .arg("control")
        .arg("--reload-rules")
        .spawn()?;

    let status = child.wait().await?;
    log::debug!("udevadm control --reload-rules exited with: {}", status);

    if let Some(path) = device_name {
        let mut child = Command::new("udevadm")
            .arg("trigger")
            .arg(format!("--name-match={}", path))
            .spawn()?;

        let status = child.wait().await?;
        log::debug!(
            "udevadm trigger --name-match={} exited with: {}",
            path,
            status
        );
    } else {
        let mut child = Command::new("udevadm").arg("trigger").spawn()?;

        let status = child.wait().await?;
        log::debug!("udevadm trigger exited with: {}", status);
    }

    // Restart ModemManager

    // - If using CLI (let's do this for
    // the moment):
    //   - "systemctl restart ModemManager"
    // - If using systemd/DBus: ?
    //   - ZBus client to systemd? ⚠️

    // => Check if ModemManager is running

    let mut child = Command::new("systemctl")
        .arg("--quiet")
        .arg("is-active")
        .arg("ModemManager")
        .spawn()?;

    if child.wait().await?.success() {
        let mut child = Command::new("systemctl")
            .arg("restart")
            .arg("ModemManager")
            .spawn()?;

        let status = child.wait().await?;
        log::debug!("systemctl restart ModemManager exited with: {}", status);
    }

    Ok(())
}

pub async fn lock_device(full_name: &str, kernel_name: &str) -> zbus::Result<()> {
    // Add udev rule to "/run/udev/rules.d"

    let file_name = format!(
        "/run/udev/rules.d/99-diagmond-blacklist-{}.rules",
        kernel_name
    );

    let file_contents = format!(
        "KERNEL==\"{}\", ENV{{ID_MM_PORT_IGNORE}}=\"1\"\n",
        kernel_name
    );

    std::fs::create_dir_all("/run/udev/rules.d")?;
    {
        let mut out_file = std::fs::File::create(file_name)?;
        write!(out_file, "{}", file_contents)?;
    }

    // ( TODO: ⚠️ ⚠️ Delete this at daemon exit in order to ensure clean state?  ⚠️ )

    reload_udev_rules(Some(full_name)).await?;

    Ok(())
}

pub async fn unlock_device(full_name: &str, kernel_name: &str) -> zbus::Result<()> {
    let file_name = format!(
        "/run/udev/rules.d/99-diagmond-blacklist-{}.rules",
        kernel_name
    );
    if std::fs::exists(&file_name)? {
        std::fs::remove_file(&file_name)?;
    }

    reload_udev_rules(Some(full_name)).await?;

    Ok(())
}
