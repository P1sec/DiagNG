meta:
  id: diag_log_config_f_req
  endian: le
  imports:
    - ../log/log_request_v1

seq:
  - id: padding
    size: 3
  - id: operation
    type: u4
    enum: log_request_v1::operation
  - id: payload
    type:
      switch-on: operation
      cases:
        'log_request_v1::operation::disable_op': log_request_v1::disable
        'log_request_v1::operation::retrieve_id_ranges_op': log_request_v1::retrieve_id_ranges
        'log_request_v1::operation::retrieve_valid_mask_op': log_request_v1::retrieve_valid_mask
        'log_request_v1::operation::set_mask_op': log_request_v1::set_mask
        'log_request_v1::operation::get_mask_op': log_request_v1::get_mask
    size-eos: true
