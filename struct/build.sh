#!/bin/bash

cd "$(dirname "$0")"

set -ex

rm -rf ../src/diagng/protocol/qualcomm/struct/* || :
rm -rf ../src/diagng/protocol/network/* || :

ksc \
    --target python \
    --read-write \
    --python-package diagng.protocol.network \
    --outdir ../src/diagng/protocol/network \
    kaitai-repo/*.ksy \
    gsmtap/*.ksy

sed -ri 's/from diagng.protocol.network import diag/from diagng.protocol.qualcomm.struct import diag/g' \
    ../src/diagng/protocol/network/gsmtap_v2.py

ksc \
    --target python \
    --read-write \
    --python-package diagng.protocol.qualcomm.struct \
    --outdir ../src/diagng/protocol/qualcomm/struct \
    qualcomm/dlf/*.ksy \
    qualcomm/diag/*.ksy \
    qualcomm/diag/command/*.ksy \
    qualcomm/diag/log/*.ksy \
    qualcomm/diag/command/subsys/diag_serv/*.ksy

sed -ri 's/from diagng.protocol.qualcomm.struct import gsmtap_v2/from diagng.protocol.network import gsmtap_v2/g' \
    ../src/diagng/protocol/qualcomm/struct/lte_rrc_ota_packet.py

for file_name in ../src/diagng/protocol/network/*; do
    if [[ -f "../src/diagng/protocol/qualcomm/struct/$(basename "${file_name}")" && "$(basename "${file_name}")" != "gsmtap_v2.py" ]]; then
        rm -f "${file_name}"
    fi
done

rm -rf ../src/diagng/protocol/qualcomm/struct/gsmtap_v2.py

cd ..
ruff format
