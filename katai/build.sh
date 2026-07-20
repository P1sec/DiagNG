#!/bin/bash

cd "$(dirname "$0")"

set -ex

ksc \
    --target python \
    --read-write \
    --python-package diagng.protocol.qualcomm.struct \
    --outdir ../src/diagng/protocol/qualcomm/struct \
    qualcomm/diag/*.ksy qualcomm/diag/command/*.ksy

cd ..
ruff format
