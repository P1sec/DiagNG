pub async fn lock_device(device_name: &str) -> zbus::Result<()> {
    log::error!("NOT IMPLEMENTED YET");

    // TODO
    // See: https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/usb_modem_pyserial.py

    Ok(())
}

pub async fn unlock_device(device_name: &str) -> zbus::Result<()> {
    log::error!("NOT IMPLEMENTED YET");

    Ok(())
}
