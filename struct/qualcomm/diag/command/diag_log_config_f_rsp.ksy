meta:
  id: diag_log_config_f_rsp
  endian: le
  imports:
    - diag_log_config_f_req
    - ../log/log_codes

seq:
  - id: padding
    size: 3
  - id: operation
    type: u4
    enum: diag_log_config_f_req::operation
  - id: status
    type: u4
    enum: status
  - id: payload
    type:
      switch-on: operation
      cases:
        'diag_log_config_f_req::operation::disable_op': disable
        'diag_log_config_f_req::operation::retrieve_id_ranges_op': retrieve_id_ranges
        'diag_log_config_f_req::operation::retrieve_valid_mask_op': retrieve_valid_mask
        'diag_log_config_f_req::operation::set_mask_op': set_mask
        'diag_log_config_f_req::operation::get_mask_op': get_mask
    size-eos: true

enums:
  status:
    0: success

types:
  # Operations:
  disable:
    seq: []
  retrieve_id_ranges:
    seq:
      - id: last_item
        type: u2
        repeat: expr
        repeat-expr: 16
  retrieve_valid_mask:
    seq:
      - id: log_mask
        type: diag_log_config_f_req::log_mask
  set_mask:
    seq:
      - id: log_mask
        type: diag_log_config_f_req::log_mask
  get_mask:
    seq:
      - id: log_mask
        type: diag_log_config_f_req::log_mask
