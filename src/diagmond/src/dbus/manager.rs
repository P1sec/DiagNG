use zbus::interface;
use zbus::object_server::SignalEmitter;

use crate::dbus::serial_device::SerialDevice;

pub struct Diagmond {
    pub usb_data: String,
    pub udev_rules: String,
    pub tokio_serial_data: String,
    pub devices: Vec<SerialDevice>,
}

// WIP 2026-06-22
// Cf. https://docs.rs/zbus/latest/zbus/attr.interface.html
// Cf. https://z-galaxy.github.io/zbus/client.html#more-advanced-example
// Cf. https://z-galaxy.github.io/zbus/service.html#a-more-complete-example

#[interface(name = "com.p1security.diagmond")]
impl Diagmond {
    #[zbus(name = "OpenSerialPort")]
    async fn open_serial_port(
        &self,
        device_path: &str
    ) { // WIP XX --> ⚠️ RETURN D-BUS OBJECT PATH TYPE?

    }

    // TODO move this to serial_device.rs, so that UDev rule-based locks
    // are released when ZBus Device objects are destroyed
    // (at app/DBus ⚠️ client connection connection close event
    // if everything goes well)
    #[zbus(name = "LockMMDeviceUDev")]
    async fn lock_mm_device_udev(
        &self,
        full_name: &str,
        kernel_name: &str,
    ) -> zbus::fdo::Result<bool> {
        log::debug!("Received: LockMMDeviceUDev({}, {})", full_name, kernel_name);
        if let Err(error) = crate::system::mm_udev_lock::lock_device(full_name, kernel_name).await {
            log::error!(
                "Could not execute LockMMDeviceUDev({}, {}): {:?}",
                full_name,
                kernel_name,
                error
            );
            return Err(zbus::fdo::Error::Failed(error.to_string()));
        }
        Ok(true)
    }

    // TODO move this to serial_device.rs, so that UDev rule-based locks
    // are released when ZBus Device objects are destroyed
    // (at app/DBus ⚠️ client connection connection close event
    // if everything goes well)
    #[zbus(name = "ReleaseMMDeviceUDev")]
    async fn release_mm_device_udev(
        &self,
        full_name: &str,
        kernel_name: &str,
    ) -> zbus::fdo::Result<bool> {
        log::debug!(
            "Received: ReleaseMMDeviceUDev({}, {})",
            full_name,
            kernel_name
        );
        if let Err(error) = crate::system::mm_udev_lock::unlock_device(full_name, kernel_name).await
        {
            log::error!(
                "Could not execute ReleaseMMDeviceUDev({}, {}): {:?}",
                full_name,
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

    #[zbus(property, name = "UDevRules")]
    async fn udev_rules(&self) -> &str {
        &self.udev_rules
    }

    #[zbus(property, name = "TokioSerialData")]
    async fn tokio_serial_data(&self) -> &str {
        &self.tokio_serial_data
    }

    #[zbus(signal, name = "UDevRulesUpdated")]
    async fn udev_rules_updated(emitter: &SignalEmitter<'_>, data: &str) -> zbus::Result<()>;

    #[zbus(signal, name = "USBDataUpdated")]
    async fn usb_data_updated(emitter: &SignalEmitter<'_>, data: &str) -> zbus::Result<()>;

    #[zbus(signal, name = "TokioSerialDataUpdated")]
    async fn tokio_serial_data_updated(emitter: &SignalEmitter<'_>, data: &str)
    -> zbus::Result<()>;
}
