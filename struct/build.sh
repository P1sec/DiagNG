#!/bin/bash

cd "$(dirname "$0")"

set -ex

rm -rf ../src/diagng/protocol/qualcomm/struct/* || :
rm -rf ../src/diagng/protocol/qualcomm/network/* || :

ksc \
    --target python \
    --read-write \
    --python-package diagng.protocol.network \
    --outdir ../src/diagng/protocol/network \
    kaitai-repo/*.ksy \
    gsmtap/*.ksy

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

cd ..
ruff format
