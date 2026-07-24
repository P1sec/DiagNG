meta:
  id: log_request_v1
  endian: le
  bit-endian: le
  imports:
    - log_codes

types:
  # Operations:
  disable:
    seq: []
  retrieve_id_ranges:
    seq: []
  retrieve_valid_mask:
    seq:
      - id: equipment_id
        type: u4
        enum: diag_logging::equipment_id
  set_mask:
    seq:
      - id: log_mask
        type: log_mask
  get_mask:
    seq: []

  # Structures:
  log_mask:
    seq:
      - id: equipment_id
        type: u4
        enum: diag_logging::equipment_id
      - id: num_logs_on_bit_field
        type: u4
      - id: logs_on_bit_field
        type: b1
        repeat: expr
        repeat-expr: num_logs_on_bit_field

enums:
  operation:
    0: disable_op
    1: retrieve_id_ranges_op
    2: retrieve_valid_mask_op # Note: Not supported by DIAG_EXT_LOG_CONFIG
    3: set_mask_op
    4: get_mask_op

