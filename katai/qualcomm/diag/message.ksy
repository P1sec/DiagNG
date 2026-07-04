meta:
  id: diag_message
  endian: le
  imports:
    - cmd_code

seq:
  - id: cmd_code
    type: u1
    enum: diag_cmd_code::diag_cmd
  - id: payload
    size-eos: true

