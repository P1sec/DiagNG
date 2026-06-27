use zbus::interface;
// use zbus::object_server::SignalEmitter;

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

pub struct Device {}

#[interface(name = "com.p1security.diagmond.Device")]
impl Device {
    // WIP XX
}

// WIP factory class:
// pub struct DeviceCreator;
