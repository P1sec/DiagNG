#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <github_tag>"
    exit 1
fi

# Make errors fatal, print commands
set -ex

cd "$(dirname "$0")"

RUST_DIR="$(git rev-parse --show-toplevel)/diagmond"

rm -rf /tmp/dist_dir /tmp/diagmond_tarball_"$1"_for_flathub_build.tar.gz

cp -rpL "${RUST_DIR}" /tmp/dist_dir

cd /tmp/dist_dir

rm -rf target/ vendor/ .flatpak-builder repo .cargo


# Fetch dependency sources to be bundled with the applicaiton
mkdir -p .cargo
cargo vendor --locked vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml

tar zcvf ../diagmond_tarball_"$1"_for_flathub_build.tar.gz .
