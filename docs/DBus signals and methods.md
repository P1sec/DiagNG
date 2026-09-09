## `diagng` D-Bus interface specifications

NOTE: `Vardict` = `a{sv}` = `Dict[str, object]` in Python

TODO: Make the services auto-activatable?

### `com.p1security.diagmetad` (Python daemon, unprivileged - may launch `diagmond`)

Properties:

* `MMDebugInfo -> string`
* `MMStatusInfo -> Vardict`
* `UDevUSBDebugInfo -> string`
* `UDevUSBDeviceTree -> Vardict`
* `UDevSPIDeviceTree -> Vardict`
* `SPIDeviceInformation -> Vardict`

Signals:

* `DiagmondLaunched ()`
* `MMInfoUpdated (Vardict mm_status_info, string mm_debug_info)`
* `UDevInfoUpdated (Vardict usb_device_tree, Vardict spi_device_tree, Vardict spi_devices, string usb_debug_info)`

Methods: 

### `com.p1security.diagmond` (Rust daemon, privilege-escalatable - session or system bus?)

Properties:

* `USBData -> string`
* `UDevRules -> string`
* `TokioSerialData -> string`
* TODO: Diag connections

Signals:

* `USBDataUpdated (string data)`
* `UDevRulesUpdated (string data)`
* `TokioSerialDataUpdated (string data)`
* TODO: Diag connections event

Methods:

* Diag-related methods
  * `OpenUSBInterface (string vid_pid, int configuration, int interface, int alt_setting) -> (ObjectPath path)` (WIP)
    * **https://docs.rs/nusb/latest/nusb/#example-usage**
    * Spawns a `/com/p1security/diagmond/SerialDevices/$NUM` object implementing the `com.p1security.diagmond.SerialDevice` interface
      * With a `Close` method to close the serial port, delete the UDev rules, unexport the object from the bus (called by `diagmond` both when closing and starting)
      * With a `Read` signal emitting bytes (`ay`)
      * With a `Write` method taking bytes (`ay`)
      * ⚠️ NOTE: This may need to take in account DETACHING THE DRIVER WHEN NEEDED (https://docs.rs/nusb/latest/nusb/struct.Device.html#method.detach_kernel_driver)
      * ➡️➡️ REUSE THE SERIALDEVICE RUST CLASS?
  * `OpenSerialPort (string device_name, string kernel_path) -> (ObjectPath path)`
    * https://www.google.com/search?q=RUST+SERIAL+PORT+COMMUNICATION
      * **https://github.com/berkowski/tokio-serial**
    * Spawns a `/com/p1security/diagmond/SerialDevices/$NUM` object implementing the `com.p1security.diagmond.SerialDevice` interface
      * With a `Close` method to close the serial port, delete the UDev rules, unexport the object from the bus (called by `diagmond` both when closing and starting)
      * With a `Read` signal emitting bytes (`ay`)
      * With a `Write` method taking bytes (`ay`)
      * (TODO: Think of putting buffering + an HDLC decoder here? MAYBE as an optional mode as operation?)

## External interfaces to dig

* Check for interesting D-Bus methods, and XDG portals to use (using the ASHPD demo application, etc.)
  * See https://github.com/P1sec/QCSuper/issues/166 ?
  * See https://github.com/P1sec/QCSuper/issues/167 ?
  * See https://www.freedesktop.org/wiki/Software/systemd/dbus/ ?
