# ADB diag setup scripts

This document specifies how the ADB Diag setup scripts, accessible from the ADB tab of DiagNG, will work.

## Auto-QC Diag enable with ARM binary transfer chain

**⚠️ Possibility: Abandon the Diag-over-TCP ADB ARM binary bridge and keep the current options of switching the USB mode through `setprop` for the moment?**

⚠️ WIP:

- How to set up the compilation chain for the ARM/ARM64 binary to be cross-compiled easily?

  - Use Docker container, Buildroot, a script downloading the NDK?
  
    - See, previously:
    
    - https://github.com/P1sec/QCSuper/tree/master/src/qcsuper/inputs/adb_bridge
    
    - + Implementation in MobileInsight (it's a JNI): https://github.com/mobile-insight/mobileinsight-mobile/tree/master/diag_revealer/qcom/jni

      - => Should we use a JNI too? (So that we can expose stuff over network, etc.)

      - See:

        - https://github.com/bbqsrc/cargo-ndk / https://archlinux.org/packages/?sort=&q=ndk&maintainer=&flagged=
        - https://aur.archlinux.org/packages?O=0&K=ndk
        - https://packages.ubuntu.com/search?keywords=ndk&searchon=names&suite=resolute&section=all

🪧 TODO:

- Scripting steps
