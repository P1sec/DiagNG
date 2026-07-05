use tokio::io::AsyncReadExt;
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
    // TODO: Push towards the client using a DBus signal
    // rather than waiting for pulling?
    // (what about buffering then?)

    #[zbus(name = "Read")]
    async fn read(&mut self) -> zbus::fdo::Result<Vec<u8>> {
        let mut buffer: [u8; 4096] = [0; 4096];
        let len_read: usize = match self.port.read(&mut buffer).await {
            Ok(obj) => obj,
            Err(err) => {
                return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
            }
        };
        Ok(buffer[..len_read].to_vec())
        // Cf. https://docs.rs/tokio/1.52.3/tokio/io/trait.AsyncReadExt.html#method.read
    }

    #[zbus(name = "Write")]
    async fn write(&mut self, data: &[u8]) -> zbus::fdo::Result<()> {
        if let Err(err) = self.port.write_all(data).await {
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        }
        Ok(())
        // Cf. https://docs.rs/tokio/1.52.3/tokio/io/trait.AsyncWriteExt.html#method.write_all
    }

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

        log::debug!("Deleting UDev rule...");

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

        // Disconnect serial port

        log::debug!("Shutting down serial port...");

        self.port.shutdown().await.ok();

        // Unregister from DBus

        let obj_server = obj_server.clone();
        let object_path = header.path().unwrap().to_owned();

        tokio::spawn(async move {
            tokio::time::sleep(std::time::Duration::from_millis(500)).await;

            log::debug!("Unregistering from D-Bus...");

            obj_server
                .remove::<Self, ObjectPath>(object_path)
                .await
                .unwrap();
        });

        log::debug!("Sending response to Close call...");

        Ok(())
    }
}
