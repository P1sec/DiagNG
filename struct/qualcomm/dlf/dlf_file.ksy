
meta:
  id: dlf_file
  endian: le
  imports:
    - ../diag/command/diag_log_f

seq:
  - id: logs
    type: diag_log_f::inner_log
    include: true
    repeat: eos
