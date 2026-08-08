meta:
  id: diag_log_f
  endian: le
  imports:
    - ../log/log_codes
    - ../log/wcdma_signaling_message
    - ../log/gsm_rr_signaling_message

# From _base_input.py in QCSuper

seq:
  - id: pending_msgs
    type: u1
  - id: log_outer_length
    type: u2
  - id: inner_log
    type: inner_log
    size: log_outer_length

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
      - id: content
        size: log_inner_length - 12
        type:
          switch-on: log_code
          cases:
            'diag_logging::log_code::wcdma_signaling_message': wcdma_signaling_message # 0x412f
            'diag_logging::log_code::gsm_rr_signaling_message': gsm_rr_signaling_message # 0x512f
            # TODO process all types supported by QCSuper in "pcap_dump.py"
    instances:
      unix_ts:
        value: |
          (log_time > 946681200 and
           log_time < 4102441200) ?
          log_time :
           315964800 +
           (log_time >> 16) / 800 +
           ((log_time & 0xffff) / 0xC000 / 800)

    enums:
      ref_ts:
        315964800: epoch_1980 # 1980-01-06 from 1970-01-01, in seconds
        946681200: min_ts_unix # 2000-01-01 from 1970-01-01, in seconds
        4102441200: max_ts_unix # 2100-01-01 from 1970-01-01, in seconds
        33067703992320000: min_ts_16bitmantissa # 2000-01-01 from 1980-01-06, in 1/800s ticks, 16 bit matissa
        198520413880320000: max_ts_16bitmantissa # 2100-01-01 from 1980-01-06, in 1/800s ticks, 16 bit matissa
        # 33067703992320000: min_ts_20bitmantissa # 2000-01-01 from 1980-01-06, in 1/50s ticks, 20 bit matissa
        # 198520413880320000: max_ts_20bitmantissa # 2100-01-01 from 1980-01-06, in 1/50s ticks, 20 bit matissa

# WIP XX
