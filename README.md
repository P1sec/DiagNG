# DiagNG 🎧 The next-generation baseband Diag client software (easily capture air traffic to PCAP - 2G/3G/4G/5G)

DiagNG is a general purpose client purpose for the diagnostic interface of Qualcomm Snapdragon basebands, present on a large part of Android phones and various USB modems.

It can be considered as a sequel for [QCSuper](https://github.com/P1sec/QCSuper), and also takes large inspiration from [SCAT](https://github.com/fgsect/scat). Like these tools, it allows to **capture 2G/3G/4G/5G air interface network traces** and save them to the [GSMTAP/PCAP](https://osmocom.org/projects/baseband/wiki/GSMTAP) format, so that you can visualize these in [Wireshark](https://www.wireshark.org/).

<p align="center">
<img src="https://github.com/P1sec/DiagNG/blob/main/packaging/screenshots/light/global-screen-focus.png?raw=true" alt="Application main screen + device screen + Wireshark">
</p>

It is an experimental, Linux-first, open-source, interoperable, brand-new way to connect to baseband USB diagnostic interfaces; whether for pedagogic or security research purposes.

It should eventually support other basebands such as Samsung Exynos processors, and why not other protocols such as AT commands.

<h1>
    <p align="center">
        <a href="https://github.com/P1sec/DiagNG/releases/download/0.1.0/com.p1security.diagng.flatpak">Download for Linux 😎 (Flatpak)</a>
    </p>
</h1>

## Table of contents

* [Feature list](#feature-list)
* [Screenshots](#screenshots)
* [Roadmap](#roadmap)
* [Legal](#legal)
* [Development environment setup](#development-environment-setup)
  * [Run project tests](#run-project-tests)
  * [Test decoder using KSV](#test-decoder-using-ksv)
  * [Technical architecture](#technical-architecture)
* [Extra resources](#extra-resources)

## Feature list

- [x] Connect a Linux raw SPI port.
- [x] Connect a Linux raw USB interface.
- [x] A sleek GTK 4/Adwaita-based UI.
- [x] SPI and USB connections are safely connected to the Python UI through a privileged Rust daemon, using a Polkit/DBus-based interface to secure privileged actions, to ensure good integration with Flatpak.
- [x] Gather phone-related information through ADB, with shortcuts to enable the QCDM USB interface easily.
- [x] Import DLF or QMDL files in order to enable interoperability with other software.
- [x] Support basic QCDM (Qualcomm diagnostic monitor) log registration.
- [x] Support basic QCDM 2G/3G/4G/5G log conversion to GSMTAP/PCAP (without advanced features such as SIB decoding, reassembly).
- [x] Wireshark plug-in management and automated installation for GSMTAP v3/5G RRC decoding (taken from SCAT).
- [x] Flatpak packaging for good integration to the Linux desktop.

## Screenshots

<p align="center">
<img src="https://github.com/P1sec/DiagNG/blob/main/packaging/screenshots/light/usb-3devices.png?raw=true" alt="Application main screen" width="838">

<img src="https://github.com/P1sec/DiagNG/blob/main/packaging/screenshots/light/qcdm-air.png?raw=true" alt="Network capture screen" width="838">

<!--img src="https://github.com/P1sec/DiagNG/blob/main/packaging/screenshots/light/modemmanager.png?raw=true" alt="ModemManager screen" width="838"-->

<img src="https://github.com/P1sec/DiagNG/blob/main/packaging/screenshots/light/adb.png?raw=true" alt="ADB devices screen" width="838">
</p>

## Roadmap

Planned for the next stable releases:
- [ ] Support for decoding IP/data packets, as present in QCSuper
- [ ] Complete QCDM to GSMTAP conversion with SIB decoding support, as present in QCSuper
- [ ] Complete QCDM to GSMTAP conversion with RRC frame reassembly support, as present in QCSuper
- [ ] QA QCDM to GSMTAP conversion with good testing protocols over real devices

Needed to cover feature gap with other softs:
- [ ] Provide good CLI functionality similar to QCSuper?
- [ ] Complete QCDM support with EFS shell decoding support, as present in QCSuper?
- [ ] Decode more QCDM logs?

Good idea to add value:
- [ ] Provide AT commands support, USIM-related commands support, QMI communication, etc.?

Wished:
- [ ] Allow to decode and register other QCDM non-OTA logs, like in SCAT?
- [ ] Support Exynos, Mediatek, HiSilicon, etc. basebands like SCAT?
- [ ] Provide more UI visualizations for QCDM features?
- [ ] Write unit tests?
- [ ] Export Kaitai Struct definitions to separate repositories/libraries?
- [ ] Take external contributions for protocolar support?
- [ ] Provide AppImage packaging?
- [ ] Provide an on-device implant to gather logs on-device, similar to QCSuper, MobileInsight, SnoopSnitch or NSG?
- [ ] Eventual Windows/macOS port?

## Legal

DiagNG is released under the [GPL v3](https://www.gnu.org/licenses/licenses.en.html) license.

DiagNG is developed with the ground of allowing the interoperability of Linux systems with baseband diagnostic interfaces, as well as of conducting security research.

P1 Security being based in France, read the following extra mentions for more detailed context on the purpose of this software:

*DiagNG est un logiciel développé à des fins de sécurité informatique et de recherche, au titre de l'article L122-6-1 du Code de la propriété intellectuelle modifié par l'article 25 de la Loi n° 2013-1168 du 18 décembre 2013 relative à la programmation militaire pour les années 2014 à 2019 et portant diverses dispositions concernant la défense et la sécurité nationale.*

*DiagNG est également développé en connaissance de l'avis du Conseil d'État, 10ème et 9ème sous-sections réunies, 16/07/2008, 301843, rendu sur saisine de l'APRIL, qui stipule que l'article L122-6-1 du Code de la propriété intellectuelle instaure bien une exception de décompilation destinée à permettre le développement de logiciels libres.*


## Development environment setup

Dependencies on Ubuntu 26.04 LTS:

```bash
sudo apt install libgirepository-2.0-dev libadwaita-1-dev \
    gir1.2-modemmanager-1.0 gir1.2-adw-1 gir1.2-gtk-4.0 \
    gir1.2-gtksource-5 libgtksourceview-5-dev \
    python3-dev blueprint-compiler cargo rustc polkitd \
    google-android-platform-tools-installer git wireshark

sudo snap install --classic astral-uv
```

Dependencies on Archlinux:

```bash
sudo pacman -S uv blueprint-compiler python-gobject \
    gtksourceview5 libadwaita libmm-glib rust polkit \
    android-tools git wireshark-qt
```

Dependencies on Fedora:

```bash
sudo dnf install uv glib2-devel libadwaita-devel gtk4-devel \
    gobject-introspection-devel python3-gobject-devel \
    python3-devel cairo-devel @development-tools \
    modemmanager-glib-devel android-tools rustc cargo \
    gtksourceview5-devel polkit git wireshark
```

Then:

```bash
cd
git clone git@github.com:P1sec/DiagNG.git diagng

cd diagng
# Download Python modules and initialize virtualenv (creates ".venv",
# call "source .venv/bin/activate" to set up)
uv sync
# Add direct commands to $PATH, so that the commands are callable
# system-wide (creates a symlink to the source in "~/.local/bin")
uv tool install -e .

sudo install -Dm644 diagmond/share/dbus-1/system.d/com.p1security.diagmond.conf \
    /etc/dbus-1/system.d/com.p1security.diagmond.conf

sudo install -Dm644 diagmond/share/polkit-1/actions/* -t /etc/polkit-1/actions/

install -Dm644 src/diagng/ui/assets/share/icons/hicolor/scalable/apps/com.p1security.diagng.svg \
    ~/.local/share/icons/com.p1security.diagng.svg

install -Dm644 src/diagng/ui/assets/share/applications/com.p1security.diagng.desktop \
    ~/.local/share/applications/com.p1security.diagng.desktop

# In one tab:
diagmond

# In another tab:
diagng
```

### Run project tests

```bash
uv run pytest
```

### Test decoder using KSV

Example command for using [`kaitai_struct_visualizer`](https://github.com/kaitai-io/kaitai_struct_visualizer):

```bash
sudo gem install kaitai-struct-visualizer

ksv \
  ~/qcsuper-dlf-samples/sample_name.dlf \
  ~/diagng/struct/qualcomm/dlf/dlf_file.ksy
```

### Technical architecture

DiagNG is meant to be split into two components:

* `com.p1security.diagng`: The main, single-instance Python 3/GTK 4/libadwaita 1.8+ front process holding a GUI, providing D-Bus session bus IPC on `/com/p1security/diagng` (including the `com.p1security.diagmetad` D-Bus interface which provides info about Linux ModemManager communication, UDev data acquisition)
  * Diag frame decoding itself is done in the Python daemon, using Kaitai struct
* `com.p1security.diagmond`: The background, privileged (runs on system bus), single-instance Rust/async process handling raw USB/SPI, USB, Diag frame acquisition, providing IPC
  * Uses `tokio-serial` + `zbus` + [`nusb`](https://github.com/kevinmehall/nusb)

This repository hence contains a modular GObject + GTK4 GUI app (leveraging GObject data models and signals, plus a decoupled UI-daemon architecture leveraging Polkit, so that we can perform serial port acquisition in a privileged fashion, and the UI and Diag decoder can be unprivileged/sandboxed too), allowing to control and manage interferences with the serial Diag port system-wide.

<p align="center">
<img src="https://github.com/P1sec/DiagNG/blob/main/packaging/screenshots/light/authorization-dialog.png?raw=true" alt="Authorization dialog" width="838">
</p>

Various information is also put in a GObject model and display it using the Adwaita UI.

It also interfaces with ModemManager, Wireshark, UDev, etc.

## Extra resources

* Related tools
  * [SCAT](https://github.com/fgsect/scat) (CLI, Python, multi-vendor)
  * [QCSuper](https://github.com/P1sec/QCSuper) (CLI, Python)
  * [MobileInsight](https://github.com/mobile-insight/mobileinsight-core) (heavier framework, mixed C++/Python)
* Protocol documentation
  * [GSMTAP v2 format](https://wiki.wireshark.org/GSMTAP)
  * [GSMTAP v3 format](https://gitea.osmocom.org/peremen/gsmtapv3/src/branch/master/GSMTAPv3.md)
  * [PCAP format definition - IETF](https://www.ietf.org/archive/id/draft-gharris-opsawg-pcap-01.html)
  * [Kaitai structure format](https://doc.kaitai.io/user_guide.html)
  * [Qualcomm Diag - Osmocom](https://osmocom.org/projects/quectel-modems/wiki/Diag)
* Research
  * [Reverse engineering a Qualcomm baseband - 28C3 - Berlin](https://fahrplan.events.ccc.de/congress/2011/Fahrplan/attachments/2022_11-ccc-qcombbdbg.pdf), Guillaume Delugré, 2011
  * [Exploiting Qualcomm WLAN And Modem Over-The-Air - Black Hat USA](https://i.blackhat.com/USA-19/Thursday/us-19-Pi-Exploiting-Qualcomm-WLAN-And-Modem-Over-The-Air.pdf) - Xiling Gong, Peter Pi, 2019
  * [QCSuper on Google Scholar](https://scholar.google.com/scholar?q=%22QCSuper%22)
