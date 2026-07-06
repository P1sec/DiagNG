use tokio::sync::mpsc::UnboundedSender;
use zbus::interface;
use zbus::object_server::SignalEmitter;

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

pub enum SerialCommand {
    Write(Vec<u8>),
    Close,
}

pub struct SerialDevice {
    pub serial_cmd_tx: UnboundedSender<SerialCommand>,
    pub device_name: String,
    pub kernel_name: String,
}

#[interface(name = "com.p1security.diagmond.SerialDevice")]
impl SerialDevice {
    // TODO: Push towards the client using a DBus signal
    // rather than waiting for pulling?
    // (what about buffering then?)

    #[zbus(signal, name = "Read")]
    async fn read(emitter: &SignalEmitter<'_>, data: Vec<u8>) -> zbus::Result<()>;

    #[zbus(signal, name = "Closed")]
    async fn closed(emitter: &SignalEmitter<'_>, reason: String) -> zbus::Result<()>;

    #[zbus(name = "Write")]
    async fn write(&self, data: Vec<u8>) -> zbus::fdo::Result<()> {
        if let Err(err) = self.serial_cmd_tx.send(SerialCommand::Write(data)) {
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        }
        Ok(())
    }

    #[zbus(name = "Close")]
    async fn close(&self) -> zbus::fdo::Result<()> {
        log::debug!(
            "Received: Close over serial port {} (KERNEL=={})",
            self.device_name,
            self.kernel_name
        );

        if let Err(err) = self.serial_cmd_tx.send(SerialCommand::Close) {
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        }

        Ok(())
    }
}
