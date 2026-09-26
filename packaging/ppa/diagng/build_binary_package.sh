#!/bin/bash

# Print commands, exit on error
set -xe

# Go to script's directory
cd "$(dirname "$0")"

PKGVER="$(grep -Po '(?<=\().+?(?=\))' debian/changelog | head -1)"

# Create a target directory for our new source package before we build it
temp_dir="$(mktemp -d)"

function cleanup_dirs {
    rm -rf "${temp_dir}"
}

trap cleanup_dirs INT TERM

cp -ra ../../.. "${temp_dir}/diagng-${PKGVER}"

cd "${temp_dir}/diagng-${PKGVER}"

rm -rf diagmond/target/ diagmond/vendor/ .flatpak-builder .venv
rm -rf packaging/flatpak/.flatpak-builder repo diagmond/.cargo .ruff_cache

mv packaging/ppa/diagng/debian .

sed -ri "s/\) bionic/staging) resolute/g" debian/changelog

debuild -b -us -uc

mv ../*.tar* ../../ || :
mv ../*.dsc* ../../ || :
mv ../*.deb* ../../ || :
mv ../*changes* ../../ || :
mv ../*build* ../../ || :
mv ../*source* ../../ || :

cleanup_dirs

echo 'Find your package in /tmp now'
