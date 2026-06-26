⚠️ WIP 2026-06-20

NOTE: `Vardict` = `a{sv}` = `Dict[str, object]` in Python

TODO: Make the services auto-activatable?

## `com.p1security.diagmetad` (Python daemon, unprivileged - launch `diagmond`?)

XX

PROPERTY:

* `DiagmondRunning -> boolean`
* `DiagmondOnSystemBus -> boolean` // Set on Diagmond.EscalatedPrivilege
* `MMDebugInfo -> string`
* `MMStatusInfo -> Vardict`
* `UDevUSBDebugInfo -> string`
* `UDevUSBDeviceTree -> Vardict`
* `UDevSPIDeviceTree -> Vardict`
* `SPIDeviceInformation -> Vardict`

SIGNAL:

* `DiagmondLaunched ()`
* `MMInfoUpdated (Vardict mm_status_info, string mm_debug_info)`
* `UDevInfoUpdated (Vardict usb_device_tree, Vardict spi_device_tree, Vardict spi_devices, string usb_debug_info)`

METHOD: 

## `com.p1security.diagmond` (Rust daemon, privilege-escalatable - session or system bus?)

XX

PROPERTY:

* `IsRunning -> boolean` (TODO: Don't, use get_name_owner?)
* `USBData -> string`
* `TokioSerialData -> string`
* TODO: Diag connections

SIGNAL:

* `USBDataUpdated (string data)`
* `TokioSerialDataUpdated (string data)`
* `EscalatedPrivilege ()` (TODO: Don't, always run as root?)
* TODO: Diag connections event

METHOD:

* WIP: Diag-related methods
  * `OpenSerialPort (string device_name) -> (boolean success, int? id)` (NEXT WIP?)
    * https://www.google.com/search?q=RUST+SERIAL+PORT+COMMUNICATION
      * **https://github.com/berkowski/tokio-serial**
    * (⚠️ ⚠️ Export a SerialPort DBus sub-interface? With Close method, TCP port prop OR Read/Write methods, etc.?)
* `TryPrivilegeEscalation () -> (boolean success)` (TODO: Don't, always run as root?)
* `LockMMDevice (string uid) -> (boolean success)`
* `ReleaseMMDevice (string uid) -> (boolean success)`
