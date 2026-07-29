#!/bin/bash

cd "$(dirname "$0")"

set -ex

rm -rf ../src/diagng/protocol/qualcomm/struct/* || :

ksc \
    --target python \
    --read-write \
    --python-package diagng.protocol.qualcomm.struct \
    --outdir ../src/diagng/protocol/qualcomm/struct \
    qualcomm/diag/*.ksy \
    qualcomm/diag/command/*.ksy \
    qualcomm/diag/log/*.ksy \
    qualcomm/diag/dlf/*.ksy \
    qualcomm/diag/command/subsys/diag_serv/*.ksy

cd ..
ruff format
