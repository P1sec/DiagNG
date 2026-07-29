meta:
  id: diag_log_f
  endian: le

# From _base_input.py in QCSuper

seq:
  - id: pending_msgs
    type: u1
  - id: log_outer_length
    type: u2
  - id: inner_log
    type: inner_log

types:
  inner_log:
    seq:
      - id: log_inner_length
        type: u2
      - id: log_code
        type: u2
      - id: log_time # <== Post-process this in code? See dlf_read.py
        type: u8
      - id: payload
        size: log_inner_length - 12

# WIP XX
