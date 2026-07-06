use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::sync::mpsc::unbounded_channel;
use tokio_serial::SerialPortBuilderExt;
use zbus::interface;
use zbus::object_server::{ObjectServer, SignalEmitter};
use zvariant::ObjectPath;

use crate::dbus::serial_device::{SerialCommand, SerialDevice, SerialDeviceSignals};

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
        &mut self,
        #[zbus(object_server)] obj_server: &ObjectServer,
        device_path: String,
        kernel_path: String,
    ) -> zbus::fdo::Result<ObjectPath<'_>> {
        // See:
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/trait.SerialPort.html#tymethod.set_timeout
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialStream.html#method.readable

        //   => https://docs.rs/tokio-serial/latest/tokio_serial/fn.new.html
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/struct.UsbPortInfo.html
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialStream.html
        //
        //   => https://github.com/berkowski/tokio-serial/blob/master/examples/serial_println.rs
        //   => https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialPortBuilder.html

        log::debug!("Opening {}...", device_path);

        let mut serial_dev = match tokio_serial::new(device_path.clone(), 115200)
            .dtr_on_open(true)
            .open_native_async()
        {
            Ok(obj) => obj,
            Err(err) => {
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };

        log::debug!("Opened {}...", device_path);

        #[cfg(unix)]
        if let Err(err) = serial_dev.set_exclusive(true) {
            log::error!("Could not lock serial port: {:?}", err);
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        }

        let (serial_cmd_tx, mut serial_cmd_rx) = unbounded_channel::<SerialCommand>();

        let dev = SerialDevice {
            serial_cmd_tx: serial_cmd_tx,
            device_name: device_path.clone(),
            kernel_name: kernel_path.clone(),
        };

        log::debug!("Reading /com/p1security/diagmond properties...");

        let object_path = ObjectPath::try_from(format!(
            "/com/p1security/diagmond/SerialDevices/{}",
            self.serial_device_ctr
        ))
        .unwrap();
        log::debug!("Listening to {}...", object_path);
        self.serial_device_ctr += 1;

        obj_server.at(&object_path, dev).await?;
        log::debug!("{} registered...", object_path);

        // Add UDev rule if ModemManager is running

        if kernel_path.len() > 0 {
            if let Err(error) =
                crate::system::mm_udev_lock::lock_device(&device_path, &kernel_path).await
            {
                log::error!(
                    "Could not add UDev lock for ModemManager device {} (KERNEL=={}): {:?}",
                    device_path,
                    kernel_path,
                    error
                );
                return Err(zbus::fdo::Error::Failed(error.to_string()));
            }
        }

        // Read port until closed

        let object_path_clone = object_path.clone();
        let obj_server = obj_server.clone();
        tokio::spawn(async move {
            let mut buffer: [u8; 4096] = [0; 4096];
            let mut reason_closed: Option<String> = None;
            loop {
                tokio::select!(
                    cmd = serial_cmd_rx.recv() => match cmd {
                        Some(operation) =>
                            match operation {
                                SerialCommand::Write(data) => {
                                    // Cf. https://docs.rs/tokio/1.52.3/tokio/io/trait.AsyncWriteExt.html#method.write_all
                                    if let Err(err) = serial_dev.write_all(&data).await {
                                        reason_closed = Some(format!("Writing to serial port failed: {:?}", err));
                                        break;
                                    }
                                    else {
                                        log::debug!(
                                            "Sent {} bytes to serial port - {}",
                                            data.len(),
                                            device_path
                                        );
                                    }
                                },
                                SerialCommand::Close => {
                                    log::info!("Closing serial port on client bail-out...");
                                    break;
                                }
                            },
                        None => {
                            reason_closed = Some(format!("MPSC channel closed"));
                            break;
                        }
                    },
                    result = serial_dev.read(&mut buffer) => match result {
                        Ok(size_read) => {
                            if size_read == 0 {
                                reason_closed = Some("Received zero-length read result on serial port".to_string());
                                break;
                            }
                            else {
                                log::debug!("Read {} bytes from serial port", size_read);

                                let object_path_clone = object_path_clone.clone();
                                {
                                    let iface_ref = match obj_server.interface::<_, SerialDevice>(object_path_clone).await {
                                        Ok(obj) => obj,
                                        Err(err) => {
                                            reason_closed = Some(format!("Serial port object destroyed: {:?}", err));
                                            break;
                                        }
                                    };

                                    // Send Read event
                                    if let Err(err) = iface_ref.read(buffer[..size_read].to_vec()).await {
                                        reason_closed = Some(format!("Could not dispatch serial port data: {:?}", err));
                                        break;
                                    }
                                }
                            }
                        },
                        Err(err) => {
                            reason_closed = Some(format!("Reading from serial port failed: {:?}", err));
                            break;
                        }
                    }
                );
            }

            if let Some(reason) = reason_closed {
                log::error!("{}", reason);

                if let Ok(iface_ref) = obj_server
                    .interface::<_, SerialDevice>(object_path_clone.clone())
                    .await
                {
                    iface_ref.closed(reason).await.ok();
                }
            }

            // Remove UDev rule if applicable

            log::debug!("Deleting UDev rule...");

            if kernel_path.len() > 0 {
                if let Err(error) =
                    crate::system::mm_udev_lock::unlock_device(&device_path, &kernel_path).await
                {
                    log::error!(
                        "Could not execute Close over serial port {} (KERNEL=={}): {:?}",
                        device_path,
                        kernel_path,
                        error
                    );
                }
            }

            // Disconnect serial port

            log::debug!("Shutting down serial port...");

            serial_dev.shutdown().await.ok();

            // Unregister from DBus

            let obj_server = obj_server.clone();

            tokio::time::sleep(std::time::Duration::from_millis(200)).await;

            log::debug!("Unregistering from D-Bus...");

            if let Err(error) = obj_server
                .remove::<SerialDevice, ObjectPath>(object_path_clone)
                .await
            {
                log::error!(
                    "Could not unregister SerialDevice object from D-Bus log: {:?}",
                    error
                )
            }
        });

        Ok(object_path)
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
