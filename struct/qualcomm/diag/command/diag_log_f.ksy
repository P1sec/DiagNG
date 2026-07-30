meta:
  id: diag_log_f
  endian: le
  imports:
    - ../log/log_codes

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
        enum: diag_logging::log_code
      - id: log_time # <== Post-process this in code? See dlf_read.py
        type: u8
      - id: payload
        size: log_inner_length - 12
    instances:
      unix_ts:
        value: |
          (log_time > 946681200 and
           log_time < 4102441200) ?
          log_time :
           315961200 +
           (log_time >> 20) / 50 +
           ((log_time & 0xfffff) / 0x100000)

    enums:
      ref_ts:
        315961200: epoch_1980 # 1980-01-06
        946681200: min_ts_unix # 2000-01-01
        4102441200: max_ts_unix # 2100-01-01

# WIP XX
