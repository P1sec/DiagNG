use zbus::interface;
use zbus::object_server::SignalEmitter;

use crate::dbus::device::Device;
use crate::system::mm_lock::{lock_device, unlock_device};

pub struct Diagmond {
    pub usb_data: String,
    pub tokio_serial_data: String,
    pub devices: Vec<Device>,
}

// WIP 2026-06-22
// Cf. https://docs.rs/zbus/latest/zbus/attr.interface.html
// Cf. https://z-galaxy.github.io/zbus/client.html#more-advanced-example
// Cf. https://z-galaxy.github.io/zbus/service.html#a-more-complete-example

#[interface(name = "com.p1security.diagmond")]
impl Diagmond {
    #[zbus(name = "LockMMDevice")]
    async fn lock_mm_device(
        &self,
        #[zbus(connection)] conn: &zbus::Connection,
        uid: &str,
    ) -> zbus::fdo::Result<bool> {
        log::debug!("Received: LockMMDevice({})", uid);
        if let Err(error) = lock_device(conn, uid).await {
            log::error!("Could not execute LockMMDevice({}): {:?}", uid, error);
        }
        Ok(true)
    }

    #[zbus(name = "ReleaseMMDevice")]
    async fn release_mm_device(
        &self,
        #[zbus(connection)] conn: &zbus::Connection,
        uid: &str,
    ) -> zbus::fdo::Result<bool> {
        log::debug!("Received: ReleaseMMDevice({})", uid);
        if let Err(error) = unlock_device(conn, uid).await {
            log::error!("Could not execute ReleaseMMDevice({}): {:?}", uid, error);
        }
        Ok(true)
    }

    #[zbus(property, name = "USBData")]
    async fn usb_data(&self) -> &str {
        &self.usb_data
    }

    #[zbus(property, name = "TokioSerialData")]
    async fn tokio_serial_data(&self) -> &str {
        &self.tokio_serial_data
    }

    #[zbus(signal, name = "USBDataUpdated")]
    async fn usb_data_updated(emitter: &SignalEmitter<'_>, data: &str) -> zbus::Result<()>;

    #[zbus(signal, name = "TokioSerialDataUpdated")]
    async fn tokio_serial_data_updated(emitter: &SignalEmitter<'_>, data: &str)
    -> zbus::Result<()>;
}
