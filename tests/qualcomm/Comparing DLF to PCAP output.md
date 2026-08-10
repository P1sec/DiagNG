# Test commands

```bash
time dlf-to-pcap ~/diagng/tests/qualcomm/dlf/sample_2g_3g_4g_xperia.dlf.gz
time qcsuper --dlf-read ~/diagng/tests/qualcomm/dlf/sample_2g_3g_4g_xperia.dlf.gz --wireshark-live
time scat --dump ~/diagng/tests/qualcomm/dlf/sample_2g_3g_4g_xperia.dlf.gz -t qc --pcap-file /tmp/scat.pcap && wireshark /tmp/scat.pcap
```

```bash
time dlf-to-pcap ~/diagng/tests/qualcomm/dlf/barberaz_5g.dlf
time qcsuper --dlf-read ~/diagng/tests/qualcomm/dlf/barberaz_5g.dlf --wireshark-live
time scat --dump ~/diagng/tests/qualcomm/dlf/barberaz_5g.dlf -t qc --pcap-file /tmp/scat.pcap && wireshark /tmp/scat.pcap
```
