meta:
  id: diag_verno_f_rsp
  endian: le

seq:
  - id: compile_date # %b %d %Y
    type: str
    encoding: ASCII
    size: 11
    pad-right: 0x20
    terminator: 0x00
  - id: compile_time # %H:%M:%S
    type: str
    encoding: ASCII
    size: 8
    pad-right: 0x20
    terminator: 0x00
  - id: release_date # %b %d %Y
    type: str
    encoding: ASCII
    size: 11
    pad-right: 0x20
    terminator: 0x00
  - id: release_time # %H:%M:%S
    type: str
    encoding: ASCII
    size: 8
    pad-right: 0x20
    terminator: 0x00
  - id: version_directory
    type: str
    encoding: ASCII
    size: 8
    pad-right: 0x20
    terminator: 0x00
  - id: station_class_mark
    type: u1
  - id: mobile_cai_revision
    type: u1
  - id: mobile_model
    type: u1
  - id: mobile_firmware_revision
    type: u1
  - id: slot_cycle_index
    type: u2
  - id: hardware_major_version
    type: u1
  - id: hardware_minor_version
    type: u1
