meta:
  id: diag_response
  endian: le
  imports:
    - cmd_code
    - command/diag_verno_f_rsp
    - command/diag_log_config_f_rsp
    - command/diag_unknown

seq:
  - id: cmd_code
    type: u1
    enum: diag_cmd_code::diag_cmd
  - id: payload
    type:
      switch-on: cmd_code
      cases:
        'diag_cmd_code::diag_cmd::verno_f': diag_verno_f_rsp
        'diag_cmd_code::diag_cmd::log_config_f': diag_log_config_f_rsp
        _: diag_unknown
    size-eos: true

