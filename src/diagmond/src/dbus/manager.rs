use tokio_serial::SerialPortBuilderExt;
use zbus::interface;
use zbus::object_server::SignalEmitter;
use zvariant::ObjectPath;

use crate::dbus::serial_device::SerialDevice;

pub struct Diagmond {
    pub usb_data: String,
    pub udev_rules: String,
    pub tokio_serial_data: String,
    pub serial_device_ctr: u64,
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
        #[zbus(connection)] conn: &zbus::Connection,
        device_path: &str,
        kernel_path: &str,
    ) -> zbus::fdo::Result<ObjectPath<'_>> {
        let serial_dev = match tokio_serial::new(device_path, 115200)
            .dtr_on_open(true)
            .open_native_async()
        {
            Ok(obj) => obj,
            Err(err) => {
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };

        let dev = SerialDevice {
            port: serial_dev,
            device_name: device_path.to_string(),
            kernel_name: kernel_path.to_string(),
        };

        let iface_ref = conn
            .object_server()
            .interface::<_, Diagmond>("/com/p1security/diagmond")
            .await?;

        let mut iface = iface_ref.get_mut().await;
        let object_path = ObjectPath::try_from(format!(
            "/com/p1security/diagmond/SerialDevices/{}",
            iface.serial_device_ctr
        ))
        .unwrap();
        iface.serial_device_ctr += 1;

        conn.object_server().at(&object_path, dev).await?;

        Ok(object_path)

        // https://docs.rs/tokio-serial/latest/tokio_serial/trait.SerialPort.html#tymethod.set_timeout
        // https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialStream.html#method.readable

        // TODO: Use
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/fn.new.html
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/struct.UsbPortInfo.html
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialStream.html
        //
        //   => https://github.com/berkowski/tokio-serial/blob/master/examples/serial_println.rs
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialPortBuilder.html
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
