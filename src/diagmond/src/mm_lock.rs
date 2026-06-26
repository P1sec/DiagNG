use zbus::{Connection, Result, proxy};

#[proxy(
    interface = "org.freedesktop.ModemManager1",
    default_service = "org.freedesktop.ModemManager1",
    default_path = "/org/freedesktop/ModemManager1"
)]
trait ModemManager {
    async fn inhibit_device(&self, uid: &str, inhibit: bool) -> Result<()>;
}

pub async fn lock_device(connection: &Connection, device_name: &str) -> Result<()> {
    let proxy = ModemManagerProxy::new(connection).await?;
    proxy.inhibit_device(device_name, true).await?;

    Ok(())
}

pub async fn unlock_device(connection: &Connection, device_name: &str) -> Result<()> {
    let proxy = ModemManagerProxy::new(connection).await?;
    proxy.inhibit_device(device_name, false).await?;

    Ok(())
}
