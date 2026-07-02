use tokio::io::AsyncWriteExt;
use zbus::message::Header;
use zbus::{ObjectServer, interface};
use zvariant::ObjectPath;
// use zbus::object_server::SignalEmitter;
use tokio_serial::SerialStream;

// NEXT TODO as of 2026-06-26 ⚠️

// See https://docs.rs/tokio-serial/latest/tokio_serial/fn.new.html
// => https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialPortBuilder.html
// => https://docs.rs/tokio-serial/latest/tokio_serial/trait.SerialPortBuilderExt.html
//     =>  ⚠️ ⚠️  https://docs.rs/tokio-serial/latest/tokio_serial/struct.SerialStream.html

// °  To expose individual device objects ⚠️ ⚠️  https://z-galaxy.github.io/zbus/service.html#using-the-objectserver
//       + ⚠️ https://docs.rs/zbus/latest/zbus/object_server/struct.ObjectServer.html#method.at
//         which is the runtime counterpart of https://docs.rs/zbus/latest/zbus/connection/struct.Builder.html#method.serve_at

// + nusb ==>
//   https://docs.rs/nusb/latest/nusb/struct.Device.html

pub struct SerialDevice {
    pub port: SerialStream,
    pub device_name: String,
    pub kernel_name: String,
}

#[interface(name = "com.p1security.diagmond.SerialDevice")]
impl SerialDevice {
    #[zbus(name = "Close")]
    async fn close(
        &mut self,
        #[zbus(header)] header: Header<'_>,
        #[zbus(object_server)] obj_server: &ObjectServer,
    ) -> zbus::fdo::Result<()> {
        log::debug!(
            "Received: Close over serial port {} (KERNEL=={})",
            self.device_name,
            self.kernel_name
        );

        // Remove UDev rule if applicable

        if self.kernel_name.len() > 0 {
            if let Err(error) =
                crate::system::mm_udev_lock::unlock_device(&self.device_name, &self.kernel_name)
                    .await
            {
                log::error!(
                    "Could not execute Close over serial port {} (KERNEL=={}): {:?}",
                    self.device_name,
                    self.kernel_name,
                    error
                );
                return Err(zbus::fdo::Error::Failed(error.to_string()));
            }
        }

        // UNREGISTER from DBus

        obj_server
            .remove::<Self, ObjectPath>(header.path().unwrap().clone())
            .await
            .unwrap();

        // Disconnect serial port

        self.port.shutdown().await.ok();

        Ok(())
    }
}

// WIP factory class:
// pub struct DeviceCreator;
