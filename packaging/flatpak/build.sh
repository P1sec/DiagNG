#!/bin/bash

# Make errors fatal, print commands
set -ex

# Move to the application's root
cd "$(dirname "$0")/../.."

# Install the required Flatpak runtime and SDK
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub --user org.gnome.Sdk//50 -y
flatpak install flathub --user org.gnome.Platform//50 -y

# Build the Flathub package
rm -rf target/ # Don't copy all the planet into the Flatpak build dir
rm -rf repo/
PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig/ flatpak-builder --install repo packaging/flatpak/com.p1security.diagng.json --user -y

sleep 2
flatpak run --user com.p1security.diagng
