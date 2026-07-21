TODO

Cf.

* https://github.com/P1sec/QCSuper/blob/master/src/qcsuper/inputs/adb_bridge/adb_bridge.c
* https://github.com/mobile-insight/mobileinsight-mobile/blob/master/diag_revealer/qcom/jni/diag_revealer.c
* https://github.com/BramBonne/snoopsnitch-pcapinterface/blob/master/SnoopSnitch/jni/diag-helper.c
* https://github.com/search?q=repo:EFForg/rayhunter+QCSuper&type=code

TODO: Because `diag_revealer.c` uses a lot of device board detection lately, should we deport some of the IOCTL communication remotely in the Python program?

=> Likely we should implement a full `diagchar` UI component? (In order to handle multiple QC Diag processors muxed into the same device, etc)
