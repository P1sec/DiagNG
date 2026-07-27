meta:
  id: ext_log_config_rsp
  endian: le
  imports:
    - ext_log_config_req
    - ../../diag_log_config_f_req

seq:
  - id: cmd_version
    type: u1
    valid:
      min: 1
      max: 2
  - id: operation
    type: u1
    enum: diag_log_config_f_req::operation
  - id: payload
    type:
      switch-on: operation
      cases:
        'diag_log_config_f_req::operation::disable_op': disable
        'diag_log_config_f_req::operation::retrieve_id_ranges_op': retrieve_id_ranges
        'diag_log_config_f_req::operation::set_mask_op': set_mask
        'diag_log_config_f_req::operation::get_mask_op': get_mask
    size-eos: true

types:
  # Operations:
  disable:
    seq:
      - id: stream_or_preset_id
        type: ext_log_config_req::stream_or_preset_id
      - id: status
        type: u8
  retrieve_id_ranges:
    seq:
      - id: status
        type: u8
      - id: reserved
        type: u8
      - id: last_item
        type: u4
        repeat: expr
        repeat-expr: 16
  retrieve_valid_mask:
    seq:
      - id: log_mask
        type: diag_log_config_f_req::log_mask
  set_mask:
    seq:
      - id: stream_or_preset_id
        type: ext_log_config_req::stream_or_preset_id
      - id: status
        type: u8
      - id: log_mask
        type: diag_log_config_f_req::log_mask
  get_mask:
    seq:
      - id: stream_or_preset_id
        type: ext_log_config_req::stream_or_preset_id
      - id: status
        type: u8
      - id: log_mask
        type: diag_log_config_f_req::log_mask

