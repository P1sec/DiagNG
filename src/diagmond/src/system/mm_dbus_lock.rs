use zbus::{Connection, Result, proxy};

#[proxy(
    interface = "org.freedesktop.ModemManager1",
    default_service = "org.freedesktop.ModemManager1",
    default_path = "/org/freedesktop/ModemManager1"
)]
trait ModemManager {
    #[zbus(name = "InhibitDevice")]
    async fn inhibit_device(&self, uid: &str, inhibit: bool) -> Result<()>;
}

pub async fn lock_device(connection: &Connection, device_name: &str) -> Result<()> {
    let proxy = ModemManagerProxy::new(connection).await?;
    proxy.inhibit_device(device_name, true).await?;

    // TODO
    // See: https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/usb_modem_pyserial.py
    // DROP INHIBITPROXY FOR NOW (BECAUSE OF https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/work_items/1075)
    // AND USE UDEV RULES INSTEAD

    // ^ WE NEED SOMETHING ELSE THAN THE DEVICE_UID FROM MODEMMANAGER
    // TO CREATE A VALID UDEV RULE THEN ??

    Ok(())
}

pub async fn unlock_device(connection: &Connection, device_name: &str) -> Result<()> {
    let proxy = ModemManagerProxy::new(connection).await?;
    proxy.inhibit_device(device_name, false).await?;

    Ok(())
}
