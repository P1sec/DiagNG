meta:
  id: log_response_v1
  endian: le
  bit-endian: le
  imports:
    - log_codes
    - log_request_v1

types:
  # Operations:
  disable:
    seq: []
  retrieve_id_ranges:
    seq:
      - id: last_item
        type: u2
        repeat: expr
        repeat-expr: 4
  retrieve_valid_mask:
    seq:
      - id: log_mask
        type: log_request_v1::log_mask
  set_mask:
    seq:
      - id: log_mask
        type: log_request_v1::log_mask
  get_mask:
    seq:
      - id: log_mask
        type: log_request_v1::log_mask

