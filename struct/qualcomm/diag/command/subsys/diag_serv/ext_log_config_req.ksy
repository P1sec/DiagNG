meta:
  id: ext_log_config_req
  endian: le
  imports:
    - ../../diag_log_config_f_req
    - ../../../log/log_codes

seq:
  - id: cmd_version
    type: u1
    valid:
      min: 1
      max: 2
  - id: operation
    type: u1
    enum: diag_log_config_f_req::operation
  - id: action
    type:
      switch-on: operation
      cases:
        'diag_log_config_f_req::operation::disable_op': disable
        'diag_log_config_f_req::operation::retrieve_id_ranges_op': retrieve_id_ranges
        'diag_log_config_f_req::operation::set_mask_op': set_mask
        'diag_log_config_f_req::operation::get_mask_op': get_mask
    size-eos: true

enums:
  stream_id:
    1: qxdm
    2: dci

  preset_id:
    1: qxdm_preset_1
    2: qxdm_preset_2

types:
  # Operations:
  disable:
    seq:
      - id: stream_or_preset_id
        type: stream_or_preset_id
      - id: reserved
        size: 1
  retrieve_id_ranges:
    seq: []
  retrieve_valid_mask:
    seq:
      - id: equipment_id
        type: u4
        enum: diag_logging::equipment_id
  set_mask:
    seq:
      - id: stream_or_preset_id
        type: stream_or_preset_id
      - id: reserved
        size: 1
      - id: log_mask
        type: diag_log_config_f_req::log_mask
  get_mask:
    seq:
      - id: stream_or_preset_id
        type: stream_or_preset_id
      - id: reserved
        size: 1
      - id: equipment_id
        type: u4
        enum: diag_logging::equipment_id

  # Structures:
  stream_or_preset_id:
    seq:
      - id: id
        type:
          switch-on: _root.cmd_version
          cases:
            1: stream_id
            2: preset_id

  stream_id:
    seq:
      - id: stream
        type: u8
        enum: stream_id

  preset_id:
    seq:
      - id: preset
        type: u8
        enum: preset_id
