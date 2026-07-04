#!/bin/bash

cd "$(dirname "$0")"

set -ex

ksc \
    --target python \
    --python-package diagng.parsing.struct.qualcomm \
    --outdir ../src/diagng/parsing/struct/qualcomm \
    qualcomm/diag/*

cd ..
ruff format
