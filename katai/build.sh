#!/bin/bash

cd "$(dirname "$0")"

set -ex

ksc \
    --target python \
    --read-write \
    --python-package diagng.parsing.struct.qualcomm \
    --outdir ../src/diagng/parsing/struct/qualcomm \
    qualcomm/diag/*.ksy qualcomm/diag/command/*.ksy

cd ..
ruff format
