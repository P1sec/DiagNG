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

    cp -ra ../../.. "${temp_dir}/diagng-${PKGVER}${version}"

    cd "${temp_dir}/diagng-${PKGVER}${version}"

    rm -rf diagmond/target/ diagmond/vendor/ .flatpak-builder .venv
    rm -rf packaging/flatpak/.flatpak-builder repo diagmond/.cargo .ruff_cache

    mv packaging/ppa/diagng/debian .

    sed -ri "s/\) bionic/${version}) ${version}/g" debian/changelog

    debuild --no-lintian -S -sa -k7BD68AA06BBE1BB41DB4D98E007F79B1496791FA

    rm -f /tmp/diagng*

    mv ../*.tar* ../../ || :
    mv ../*.dsc* ../../ || :
    mv ../*.deb* ../../ || :
    mv ../*changes* ../../ || :
    mv ../*build* ../../ || :
    mv ../*source* ../../ || :

    # Push to Launchpad

    dput ppa:marin-m/p1sec-foss "../../diagng_${PKGVER}${version}_source.changes"

    cd "${ORIG_DIR}"

    rm -rf "${temp_dir}/diagng-${PKGVER}${version}"

done

cleanup_dirs

echo 'Package successfully uploaded to Launchpad, find it in /tmp'
