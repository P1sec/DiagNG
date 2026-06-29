pub async fn lock_device(full_name: &str, kernel_name: &str) -> zbus::Result<()> {
    // TODO - Implement this feature based of QCSuper logic
    // See: https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/usb_modem_pyserial.py

    log::error!("NOT IMPLEMENTED YET");

    // TODO: Add udev rule to "/run/udev/rules.d"

    // FILE NAME: "/run/udev/rules.d/99-diagmond-blacklist-%s.rules" % kernel_name

    // FILE CONTENTS: 'KERNEL=="%s", ENV{ID_MM_PORT_IGNORE}="1"\n' % kernel_name

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
    log::error!("NOT IMPLEMENTED YET");

    Ok(())
}
