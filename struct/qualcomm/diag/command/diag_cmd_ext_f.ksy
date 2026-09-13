meta:
  id: diag_cmd_ext_f
  endian: le
  imports:
    - ../response

seq:
  - id: version
    type: u1
    valid:
      min: 1
  - id: header
    type:
      switch-on: version
      cases:
        1: v1_header
        2: v2_header
  - id: payload
    type: diag_response

types:
  v1_header:
    seq:
      - id: proc_id
        type: u2
        enum: proc_type
      - id: id
        type: u4

  v2_header:
    seq:
      - id: proc_id
        type: u2
        enum: proc_type
      - id: len_name
        type: u1
      - id: time_offset_type
        type: u1
        enum: time_offset_type
      - id: time_offset
        type: u8
      - id: ulog_name
        type: strz
        encoding: ASCII
        size: 24

enums:
  time_offset_type:
    0: no_custom_offset
    1: sync_offset_type
    255: no_offset
  proc_type:
    0: modem
    1: app
    2: common_dual
    3: qdsp6
    4: riva
    5: slpi
    6: wdsp
    7: cdsp
    255: no_proc

