use std::io::Write;

pub async fn lock_device(full_name: &str, kernel_name: &str) -> zbus::Result<()> {
    // TODO - Implement this feature based of QCSuper logic
    // See: https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/usb_modem_pyserial.py

    log::error!("NOT FULLY IMPLEMENTED YET");

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

    // MANPAGE TO READ URL: https://man7.org/linux/man-pages/man7/udev.7.html

    // TODO: Sync code contained in "udev_rules_dir.py"

    // TODO: Reload udev rules (➡️ through which channel?)

    // If using CLI:
    //  - "udevadm control --reload-rules"
    //  - "udevadm trigger --name-match=%s" % full_name (TODO: why?)
    // If using another channel: ?

    // TODO: Restart ModemManager (➡️ through which channel?)

    // If using CLI:
    //  - "systemctl restart ModemManager"
    //  - If using systemd/DBus: ?
    //    - ZBus client to systemd? ⚠️

    Ok(())
}

pub async fn unlock_device(full_name: &str, kernel_name: &str) -> zbus::Result<()> {
    // TODO - Implement this feature based of QCSuper logic
    // See: https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/usb_modem_pyserial.py

    log::error!("NOT FULLY IMPLEMENTED YET");

    let file_name = format!(
        "/run/udev/rules.d/99-diagmond-blacklist-{}.rules",
        kernel_name
    );
    if std::fs::exists(&file_name)? {
        std::fs::remove_file(&file_name)?;
    }

    // TODO: Sync code contained in "udev_rules_dir.py"

    // TODO: Reload udev rules (➡️ through which channel?)

    // TODO: Restart ModemManager (➡️ through which channel?)

    Ok(())
}
