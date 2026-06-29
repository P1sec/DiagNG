pub async fn lock_device(kernel_name: &str) -> zbus::Result<()> {
    log::error!("NOT IMPLEMENTED YET");

    // TODO - Implement this feature based of QCSuper logic
    // See: https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/usb_modem_pyserial.py

    // TODO: Add udev rule to "/run/udev/rules.d"

    // FILE NAME: XX

    // FILE CONTENTS: XX
    //  => FILTER SELECTOR: XX

    // MANPAGE TO READ URL: XX

    // TODO: Sync code contained in "udev_rules_dir.py"
    // TODO: Reload udev rules (➡️ through which channel?)
    // TODO: Restart ModemManager (➡️ through which channel?)

    Ok(())
}

pub async fn unlock_device(kernel_name: &str) -> zbus::Result<()> {
    log::error!("NOT IMPLEMENTED YET");

    Ok(())
}
