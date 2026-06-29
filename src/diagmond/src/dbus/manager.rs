use zbus::interface;
use zbus::object_server::SignalEmitter;

use crate::dbus::device::Device;

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
    #[zbus(name = "LockMMDeviceUDev")]
    async fn lock_mm_device_udev(&self, kernel_name: &str) -> zbus::fdo::Result<bool> {
        log::debug!("Received: LockMMDeviceUDev({})", kernel_name);
        if let Err(error) = crate::system::mm_udev_lock::lock_device(kernel_name).await {
            log::error!(
                "Could not execute LockMMDeviceUDev({}): {:?}",
                kernel_name,
                error
            );
            return Err(zbus::fdo::Error::Failed(error.to_string()));
        }
        Ok(true)
    }

    #[zbus(name = "ReleaseMMDeviceUDev")]
    async fn release_mm_device_udev(&self, kernel_name: &str) -> zbus::fdo::Result<bool> {
        log::debug!("Received: ReleaseMMDeviceUDev({})", kernel_name);
        if let Err(error) = crate::system::mm_udev_lock::unlock_device(kernel_name).await {
            log::error!(
                "Could not execute ReleaseMMDeviceUDev({}): {:?}",
                kernel_name,
                error
            );
            return Err(zbus::fdo::Error::Failed(error.to_string()));
        }
        Ok(true)
    }

    /* #[zbus(name = "LockMMDeviceDBus")]
    async fn lock_mm_device_dbus(
        &self,
        #[zbus(connection)] conn: &zbus::Connection,
        uid: &str,
    ) -> zbus::fdo::Result<bool> {
        log::debug!("Received: LockMMDeviceDBus({})", uid);
        if let Err(error) = crate::system::mm_dbus_lock::lock_device(conn, uid).await {
            log::error!("Could not execute LockMMDeviceDBus({}): {:?}", uid, error);
            return Err(zbus::fdo::Error::Failed(error.to_string()));
        }
        Ok(true)
    }

    #[zbus(name = "ReleaseMMDeviceDBus")]
    async fn release_mm_device_dbus(
        &self,
        #[zbus(connection)] conn: &zbus::Connection,
        uid: &str,
    ) -> zbus::fdo::Result<bool> {
        log::debug!("Received: ReleaseMMDeviceDBus({})", uid);
        if let Err(error) = crate::system::mm_dbus_lock::unlock_device(conn, uid).await {
            log::error!("Could not execute ReleaseMMDeviceDBus({}): {:?}", uid, error);
            return Err(zbus::fdo::Error::Failed(error.to_string()));
        }
        Ok(true)
    } */

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
