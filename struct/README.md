# DiagNG struture repository

This folder contains various binary data structures used by DiagNG, declared in the [Kaitai Structure](https://kaitai.io/) (.ksy) format, and subsequently converted into Python using the `build.sh` script present in the current directory.

Kaitai Struct uses a [YAML](https://en.wikipedia.org/wiki/YAML)-based format.

* Examples of using enumerations:
  * https://doc.kaitai.io/user_guide.html#enums
    * https://doc.kaitai.io/user_guide.html#delimited-struct
    * https://doc.kaitai.io/user_guide.html#delimited-struct-advanced
    * https://doc.kaitai.io/user_guide.html#custom-process
  * https://formats.kaitai.io/swf/

Examples of existing structures can be ported from existing projects such as [SCAT](https://github.com/fgsect/scat) or Wireshark.

* Cf. https://github.com/fgsect/scat/blob/v2.0.0/src/scat/parsers/qualcomm/diagcmd.py
* Cf. https://www.wireshark.org/docs/wsar_html/packet-qcdiag_8h_source.html

Prior to implementing code, structures can be decoded using individually using a too such as the Kaitai web IDE or `ksv` / `kaitai-struct-visualizer`.

* https://ide.kaitai.io/
* https://github.com/kaitai-io/kaitai_struct_visualizer
* https://github.com/kaitai-io/awesome-kaitai
