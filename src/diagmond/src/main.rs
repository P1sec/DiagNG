// WIP: See README.md
//  + https://github.com/diwic/dbus-rs/blob/master/dbus-tokio/examples/tokio_server_cr.rs
//  + https://github.com/diwic/dbus-rs/blob/master/dbus-tokio/examples/tokio_adv_server_cr.rs

mod logging;
mod usb;

use crate::logging::Logging;
use crate::usb::{UsbDevicesEndpointResp, get_usb_metadata};
use futures_util::StreamExt;

#[tokio::main]
async fn main() {
    // Set up logging
    Logging::setup_logging_main_proc();

    // Connect to the session bus
    let (resource, conn) = dbus_tokio::connection::new_session_sync().unwrap();

    // The resource is a task that should be spawned onto a tokio compatible
    // reactor ASAP. If the resource ever finishes, you lost connection to D-Bus.
    //
    // To shut down the connection, both call _handle.abort() and drop the connection.
    let _handle = tokio::spawn(async {
        let err = resource.await;
        panic!("Lost connection to D-Bus: {}", err);
    });

    // Register a DBus named service, using a well-known name
    // Don't allow takover of our own service name
    // (TODO: Handle concurrent processes?)
    conn.request_name("com.p1security.diagmond", false, true, false)
        .await
        .unwrap();

    // WIP: Spawn USB parsing code and retrieve JSON serialized
    // contents + send it back through JSON-RPC when we have connections

    let mut hotplug_watch = nusb::watch_devices().unwrap();

    loop {
        let devices: UsbDevicesEndpointResp = get_usb_metadata().await;

        let _devices_resp_string = serde_json::to_string(&devices).unwrap();
        log::info!(
            "USB data received: {}",
            serde_json::to_string_pretty(&devices).unwrap()
        );

        // NEXT TODO: 2026-06-18:
        //  -> Send the DBus-serialized JSON data to the Python
        // process (and eventually display it to the UI)

        let next_event = hotplug_watch.next().await.unwrap();
        log::info!("USB event received: {:?}", next_event);
    }
}
