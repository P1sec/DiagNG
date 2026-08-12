meta:
  id: gsmtap
  endian: be
  bit-endian: be
  imports:
    - gsmtap_v2
    - gsmtap_v3

# From: https://github.com/osmocom/libosmocore/blob/master/include/osmocom/core/gsmtap.h

seq:
  - id: version
    type: u1
    valid:
      min: 1
      max: 3
  - id: content
    type:
      switch-on: version
      cases:
        2: gsmtap_v2
        3: gsmtap_v3
    size-eos: true

# TODO XX
