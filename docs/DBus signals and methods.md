⚠️ WIP 2026-06-20

NOTE: `Vardict` = `a{sv}` = `Dict[str, object]` in Python

TODO: Make the services auto-activatable?

## `com.p1security.diagng` (main Python process, provides UI, unprivileged)

XX

PROPERTY:

SIGNAL: `

METHOD: 

## `com.p1security.diagmetad` (Python daemon, unprivileged - launch `diagmond` and store the privesc status?)

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
* `USBData -> Vardict`
* TODO: Diag connections

SIGNAL:

* `USBDataUpdated (Vardict data)`
* `EscalatedPrivilege ()` (TODO: Don't, always run as root?)
* TODO: Diag connections event

METHOD:

* `TryPrivilegeEscalation () -> (boolean success)` (TODO: Don't, always run as root?)
* `LockMMDevice (string uid) -> (boolean success)`
* `ReleaseMMDevice (string uid) -> (boolean success)`
* TODO: Diag-related methods
