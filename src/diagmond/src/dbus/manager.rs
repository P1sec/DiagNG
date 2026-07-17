use nusb::descriptors::TransferType;
use nusb::list_devices;
use nusb::transfer::{Bulk, Direction, In, Out};
use std::sync::Mutex;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::sync::mpsc::unbounded_channel;
use tokio_serial::SerialPortBuilderExt;
use zbus::interface;
use zbus::object_server::{ObjectServer, SignalEmitter};
use zvariant::ObjectPath;

use crate::dbus::serial_device::{SerialCommand, SerialDevice, SerialDeviceSignals};

pub struct Diagmond {
    pub usb_data: String,
    pub usb_data_pretty: String,
    pub udev_rules: String,
    pub tokio_serial_data: String,
    pub serial_device_ctr: Mutex<u64>,
}

// WIP 2026-06-22
// Cf. https://docs.rs/zbus/latest/zbus/attr.interface.html
// Cf. https://z-galaxy.github.io/zbus/client.html#more-advanced-example
// Cf. https://z-galaxy.github.io/zbus/service.html#a-more-complete-example

#[interface(name = "com.p1security.diagmond")]
impl Diagmond {
    #[zbus(name = "OpenUSBInterface")]
    async fn open_usb_interface(
        &self,
        #[zbus(object_server)] obj_server: &ObjectServer,
        device_path: String,
        kernel_path: String,
        bus_id: String,
        port_chain: Vec<u8>,
        vid: u16,
        pid: u16,
        configuration_id: u8,
        interface_id: u8,
        alt_setting_id: u8,
    ) -> zbus::fdo::Result<ObjectPath<'_>> {
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

        let mut devices = match list_devices().await {
            Ok(obj) => obj,
            Err(err) => {
                log::error!("Could not list USB devices: {:?}", err);
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };

        let device_info = match devices.find(|dev| {
            dev.bus_id() == bus_id
                && dev.port_chain().to_vec() == port_chain
                && dev.vendor_id() == vid
                && dev.product_id() == pid
        }) {
            Some(obj) => obj,
            None => {
                log::error!("Could not find USB device");
                return Err(zbus::fdo::Error::Failed(
                    "Could not find USB device".to_string(),
                ));
            }
        };

        let device = match device_info.open().await {
            Ok(obj) => obj,
            Err(err) => {
                log::error!("Could not open USB device: {:?}", err);
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };

        device.detach_kernel_driver(interface_id).ok();

        let mut is_configured: bool = false;
        if let Ok(configuration) = device.active_configuration() {
            if configuration.configuration_value() == configuration_id {
                is_configured = true;
            }
        }
        if !is_configured {
            if let Err(err) = device.set_configuration(configuration_id).await {
                log::error!("Could not set USB device configuration: {:?}", err);
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            };
        }

        let interface = match device.claim_interface(interface_id).await {
            Ok(obj) => obj,
            Err(err) => {
                log::error!("Could not claim USB device interface: {:?}", err);
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };

        if let Err(err) = interface.set_alt_setting(alt_setting_id).await {
            log::error!("Could not set USB alternate setting: {:?}", err);
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        };

        let intf_descriptor = match interface.descriptor() {
            Some(obj) => obj,
            None => {
                log::error!("Could not retrieve USB interface descriptor");
                return Err(zbus::fdo::Error::Failed(
                    "Could not retrieve USB interface descriptor".to_string(),
                ));
            }
        };

        for endpoint in intf_descriptor.endpoints() {
            log::debug!(
                "Found descriptor on device: direction={:?}, transfer_type={:?}, mtu={:?}",
                endpoint.direction(),
                endpoint.transfer_type(),
                endpoint.max_packet_size()
            );
        }

        let out_endpoint_addr = match intf_descriptor.endpoints().find(|endpoint| {
            endpoint.direction() == Direction::Out && endpoint.transfer_type() == TransferType::Bulk
        }) {
            Some(obj) => obj,
            None => {
                log::error!("Could not find outbound descriptor");
                return Err(zbus::fdo::Error::Failed(
                    "Could not find outbound descriptor".to_string(),
                ));
            }
        }
        .address();

        let in_endpoint_addr = match intf_descriptor.endpoints().find(|endpoint| {
            endpoint.direction() == Direction::In && endpoint.transfer_type() == TransferType::Bulk
        }) {
            Some(obj) => obj,
            None => {
                log::error!("Could not find inbound descriptor");
                return Err(zbus::fdo::Error::Failed(
                    "Could not find inbound descriptor".to_string(),
                ));
            }
        }
        .address();

        let out_endpoint = match interface.endpoint::<Bulk, Out>(out_endpoint_addr) {
            Ok(obj) => obj,
            Err(err) => {
                log::error!("Could not open USB outbound descriptor: {:?}", err);
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };

        let in_endpoint = match interface.endpoint::<Bulk, In>(in_endpoint_addr) {
            Ok(obj) => obj,
            Err(err) => {
                log::error!("Could not open USB inbound descriptor: {:?}", err);
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };

        let mut out_writer = out_endpoint.writer(4096);

        let mut in_reader = in_endpoint.reader(4096);

        let (serial_cmd_tx, mut serial_cmd_rx) = unbounded_channel::<SerialCommand>();

        let dev = SerialDevice {
            serial_cmd_tx: serial_cmd_tx,
        };

        log::debug!("Reading /com/p1security/diagmond properties...");

        let object_path = ObjectPath::try_from(format!(
            "/com/p1security/diagmond/SerialDevices/{}",
            self.serial_device_ctr.lock().unwrap()
        ))
        .unwrap();
        {
            let mut guard = self.serial_device_ctr.lock().unwrap();
            *guard += 1;
        }
        log::debug!("Trying to register {}...", object_path);

        if let Err(err) = obj_server.at(&object_path, dev).await {
            log::error!("Could not register ZBus secondary interface: {:?}", err);
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        }
        log::debug!("{} registered...", object_path);

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
                                if let Err(err) = out_writer.write_all(&data).await {
                                    reason_closed = Some(format!("Writing to serial USB interface: {:?}", err));
                                    break;
                                }
                                else {
                                    if let Err(err) = out_writer.flush().await {
                                        reason_closed = Some(format!("Flushing to serial USB interface: {:?}", err));
                                        break;
                                    }
                                    log::debug!(
                                        "Sent {} bytes to USB interface",
                                        data.len()
                                    );
                                }
                            },
                            SerialCommand::Close => {
                                log::info!("Closing USB interface on client bail-out...");
                                break;
                            }
                        },
                        None => {
                            reason_closed = Some(format!("MPSC channel closed"));
                            break;
                        }
                    },
                    result = in_reader.read(&mut buffer) => match result {
                        Ok(size_read) => {
                            if size_read == 0 {
                                reason_closed = Some("Received zero-length read result on USB interface".to_string());
                                break;
                            }
                            else {
                                log::debug!("Read {} bytes from USB interface", size_read);

                                let object_path_clone = object_path_clone.clone();
                                {
                                    let iface_ref = match obj_server.interface::<_, SerialDevice>(object_path_clone).await {
                                        Ok(obj) => obj,
                                        Err(err) => {
                                            reason_closed = Some(format!("USB interface object destroyed: {:?}", err));
                                            break;
                                        }
                                    };

                                    // Send Read event
                                    if let Err(err) = iface_ref.read(buffer[..size_read].to_vec()).await {
                                        reason_closed = Some(format!("Could not dispatch USB interface data: {:?}", err));
                                        break;
                                    }
                                }
                            }
                        },
                        Err(err) => {
                            reason_closed = Some(format!("Reading from USB interface failed: {:?}", err));
                            break;
                        }
                    }
                );
            }

            // Disconnect USB interface

            log::debug!("Shutting down USB interface...");

            if let Err(err) = out_writer.shutdown().await {
                log::warn!("Could not shutdown writer: {:?}", err);
            };

            if let Err(err) = device.attach_kernel_driver(interface_id) {
                log::warn!("Could not reattach kernel drivers: {:?}", err);
            };

            // Notify clients of close operation

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
                        "Could not execute Close over USB interface {} (KERNEL=={}): {:?}",
                        device_path,
                        kernel_path,
                        error
                    );
                }
            }

            // Unregister from DBus

            let obj_server = obj_server.clone();

            tokio::time::sleep(std::time::Duration::from_millis(200)).await;

            log::debug!("Unregistering from D-Bus...");

            if let Err(error) = obj_server
                .remove::<SerialDevice, ObjectPath>(object_path_clone)
                .await
            {
                log::error!(
                    "Could not unregister SerialDevice object from D-Bus tree: {:?}",
                    error
                )
            }
        });

        Ok(object_path)
    }

    #[zbus(name = "OpenSerialPort")]
    async fn open_serial_port(
        &self,
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

        #[cfg(target_os = "linux")]
        if !(device_path.starts_with("/dev/ttyHS") || device_path.starts_with("/dev/ttyUSB")) {
            let reason = format!("Invalid TTY device path: {}", device_path);
            log::error!("{}", reason);
            return Err(zbus::fdo::Error::Failed(reason));
        }

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
        };

        log::debug!("Reading /com/p1security/diagmond properties...");

        let object_path = ObjectPath::try_from(format!(
            "/com/p1security/diagmond/SerialDevices/{}",
            self.serial_device_ctr.lock().unwrap()
        ))
        .unwrap();
        {
            let mut guard = self.serial_device_ctr.lock().unwrap();
            *guard += 1;
        }
        log::debug!("Trying to register {}...", object_path);

        if let Err(err) = obj_server.at(&object_path, dev).await {
            log::error!("Could not register ZBus secondary interface: {:?}", err);
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        }
        log::debug!("{} registered...", object_path);

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
                                            "Sent {} bytes to serial port",
                                            data.len()
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

            // Disconnect serial port

            log::debug!("Shutting down serial port...");

            serial_dev.shutdown().await.ok();

            // Notify clients of close operation

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

            // Unregister from DBus

            let obj_server = obj_server.clone();

            tokio::time::sleep(std::time::Duration::from_millis(200)).await;

            log::debug!("Unregistering from D-Bus...");

            if let Err(error) = obj_server
                .remove::<SerialDevice, ObjectPath>(object_path_clone)
                .await
            {
                log::error!(
                    "Could not unregister SerialDevice object from D-Bus tree: {:?}",
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

    #[zbus(property, name = "USBDataPretty")]
    async fn usb_data_pretty(&self) -> &str {
        &self.usb_data_pretty
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
    async fn usb_data_updated(
        emitter: &SignalEmitter<'_>,
        data: &str,
        pretty_data: &str,
    ) -> zbus::Result<()>;

    #[zbus(signal, name = "TokioSerialDataUpdated")]
    async fn tokio_serial_data_updated(emitter: &SignalEmitter<'_>, data: &str)
    -> zbus::Result<()>;
}
