#!/bin/bash

# Print commands, exit on error
set -xe

# Go to script's directory
cd "$(dirname "$0")"

PKGVER="$(grep -Po '(?<=\().+?(?=\))' debian/changelog | head -1)"

ORIG_DIR="$(pwd)"

# Create a target directory for our new source package before we build it
temp_dir="$(mktemp -d)"

function cleanup_dirs {
    rm -rf "${temp_dir}"
}

trap cleanup_dirs INT TERM

for version in resolute stonking; do

    cp -ra ../../../diagmond "${temp_dir}/diagmond-${PKGVER}${version}"
    cp -ra debian "${temp_dir}/diagmond-${PKGVER}${version}/"

    cd "${temp_dir}/diagmond-${PKGVER}${version}"

    rm -rf target/ vendor/ .cargo

    mkdir -p .cargo
    cargo vendor --locked vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml

    # "dpkg-source" will destroy the ".gitignore" files from source archive anyway.
    # Prevent "cargo" to check for their presence.
    find vendor -name .cargo-checksum.json -exec sed -ri 's/"[^"]*?\.gitignore":"[^"]+?"[,\}]//g' '{}' \;
    find vendor -name .cargo-checksum.json -exec sed -ri 's/"[^"]*?\.orig":"[^"]+?"[,\}]//g' '{}' \;
    find vendor -name .cargo-checksum.json -exec sed -ri 's/"[^"]*?\.a":"[^"]+?"[,\}]//g' '{}' \;
    find vendor -name .cargo-checksum.json -exec sed -ri 's/"[^"]*?\.mailmap":"[^"]+?"[,\}]//g' '{}' \;
    find vendor -name .cargo-checksum.json -exec sed -ri 's/"[^"]*?\.gitmodules":"[^"]+?"[,\}]//g' '{}' \;
    find vendor -name .cargo-checksum.json -exec sed -ri 's/"[^"]*?\.lock":"[^"]+?"[,\}]//g' '{}' \;
    
    sed -ri "s/\) bionic/${version}) ${version}/g" debian/changelog

    debuild --no-lintian -S -sa -k7BD68AA06BBE1BB41DB4D98E007F79B1496791FA

    rm -f /tmp/diagmond*

    mv ../*.tar* ../../ || :
    mv ../*.dsc* ../../ || :
    mv ../*.deb* ../../ || :
    mv ../*changes* ../../ || :
    mv ../*build* ../../ || :
    mv ../*source* ../../ || :

    # Push to Launchpad

    dput ppa:marin-m/p1sec-foss "../../diagmond_${PKGVER}${version}_source.changes"

    cd "${ORIG_DIR}"

    rm -rf "${temp_dir}/diagmond-${PKGVER}${version}"

done

cleanup_dirs

echo 'Package successfully uploaded to Launchpad, find it in /tmp'
