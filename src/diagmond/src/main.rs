pub mod logging;
pub mod system {
    // pub mod mm_dbus_lock;
    pub mod mm_udev_lock;
    pub mod serial_devices;
    pub mod udev_rules;
    pub mod usb_devices;
    pub mod usb_devices_pretty;
}
pub mod dbus {
    pub mod manager;
    pub mod serial_device;
}

use crate::dbus::manager::{Diagmond, DiagmondSignals};
use crate::logging::Logging;
use crate::system::serial_devices::list_devices;
use crate::system::udev_rules::get_udev_rules_data;
use crate::system::usb_devices::{UsbDevicesEndpointResp, get_usb_metadata};
use crate::system::usb_devices_pretty::{UsbDeviceTreePretty, device_tree_to_pretty};

#[cfg(target_os = "linux")]
use std::os::unix::process::CommandExt;

use futures_util::StreamExt;
use tokio_serial::SerialPortInfo;
use zbus::connection::Builder;
use zbus::fdo::{ObjectManager, RequestNameFlags};

#[tokio::main]
async fn main() -> zbus::Result<()> {
    // Set up logging
    Logging::setup_logging_main_proc();

    #[cfg(target_os = "linux")]
    if nix::unistd::geteuid().as_raw() != 0 {
        let args: Vec<String> = std::env::args().collect();
        let _ = std::process::Command::new("pkexec").args(args).exec();
        log::error!("Could not launch pkexec");
        std::process::exit(1);
    }

    let udev_rules = get_udev_rules_data(false).await?;

    let diagmond = Diagmond {
        usb_data: "null".to_string(),
        usb_data_pretty: "null".to_string(),
        udev_rules: serde_json::to_string_pretty(&udev_rules).unwrap(), // WIP
        tokio_serial_data: "null".to_string(),
        serial_device_ctr: 1,
    };

    let connection = Builder::system()?
        .serve_at("/com/p1security/diagmond", diagmond)?
        .serve_at("/com/p1security/diagmond", ObjectManager {})?
        .serve_at("/com/p1security/diagmond/SerialDevices", ObjectManager {})?
        .build()
        .await?;

    if let Err(err) = connection
        .request_name_with_flags(
            "com.p1security.diagmond",
            RequestNameFlags::DoNotQueue.into(),
        )
        .await
    {
        log::error!("Could not register D-Bus service: {:?}", err);
        std::process::exit(1);
    }

    // If we can acquire the bus, prune any stale UDev rules

    let udev_rules = get_udev_rules_data(true).await?;
    let udev_rules = serde_json::to_string_pretty(&udev_rules).unwrap();

    // Trigger the DBus property change
    {
        let iface_ref = connection
            .object_server()
            .interface::<_, Diagmond>("/com/p1security/diagmond")
            .await?;

        let mut iface = iface_ref.get_mut().await;
        iface.udev_rules = udev_rules.clone();
    }

    // Spawn inotify watch over /run/udev/rules.d
    tokio::spawn(crate::system::udev_rules::watch_udev_rules(
        connection.clone(),
    ));

    // Spawn USB parsing code and retrieve JSON serialized
    // contents + send it back through D-Bus when we have connections
    let mut hotplug_watch = nusb::watch_devices().unwrap();

    loop {
        let usb_devices: UsbDevicesEndpointResp = get_usb_metadata().await;
        let devices_resp_string = serde_json::to_string_pretty(&usb_devices).unwrap();

        let usb_devices_pretty: UsbDeviceTreePretty = device_tree_to_pretty(usb_devices);
        let devices_resp_pretty = serde_json::to_string_pretty(&usb_devices_pretty).unwrap();

        log::info!("USB devices list received");

        let serial_devices: Vec<SerialPortInfo> = list_devices();

        let serial_devices_string = serde_json::to_string_pretty(&serial_devices).unwrap();
        log::info!("Serial devices list received");

        // Trigger the DBus property change
        {
            let iface_ref = connection
                .object_server()
                .interface::<_, Diagmond>("/com/p1security/diagmond")
                .await?;

            let mut iface = iface_ref.get_mut().await;
            iface.usb_data = devices_resp_string.clone();
            iface.usb_data_pretty = devices_resp_pretty.clone();
            iface.tokio_serial_data = serial_devices_string.clone();

            // Send the DBus-serialized JSON data to the Python
            // process (and eventually display it to the UI)

            iface_ref
                .usb_data_updated(&devices_resp_string, &devices_resp_pretty)
                .await?;
            iface_ref
                .tokio_serial_data_updated(&serial_devices_string)
                .await?;
        }

        let next_event = hotplug_watch.next().await.unwrap();
        log::info!("USB event received: {:?}", next_event);
    }
}
