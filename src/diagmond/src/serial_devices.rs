// WIP XX Use tokio_serial::available_ports() and ⚠️ send it over D-Bus

use tokio_serial::{SerialPortInfo, available_ports};

pub fn list_devices() -> Vec<SerialPortInfo> {
    available_ports().unwrap().into()
}
