use tokio::sync::mpsc::UnboundedSender;
use zbus::interface;
use zbus::object_server::SignalEmitter;

pub enum SerialCommand {
    Write(Vec<u8>),
    Close,
}

pub struct SerialDevice {
    pub serial_cmd_tx: UnboundedSender<SerialCommand>,
}

#[interface(name = "com.p1security.diagmond.SerialDevice")]
impl SerialDevice {
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
        if let Err(err) = self.serial_cmd_tx.send(SerialCommand::Close) {
            return Err(zbus::fdo::Error::Failed(format!("{:?}", err)));
        }

        Ok(())
    }
}
