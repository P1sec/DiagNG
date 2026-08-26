<p align="center">
<img src="https://github.com/P1sec/DiagNG/blob/main/docs/project_banner.png" alt="Landing illustration">
</p>

# DiagNG 🎧 The next-generation baseband Diag client software (2G/3G/4G/5G)

DiagNG is a general purpose client purpose for the diagnostic interface of the Qualcomm Snapdragon basebands. It should eventually support other basebands such as Samsung Exynos processors.

This software is a work-in-progress intended sequel (v3) for [QCSuper](https://github.com/P1sec/QCSuper).

<center>[TODO: Screenshot]</center>

<center>[TODO: Flathub download badge]</center>

Feature list:

* TODO

## Legal

DiagNG is released under the GPL v3 license.

DiagNG is developed with the ground of allowing the interoperability of Linux system with baseband diagnostic interfaces, as well of conducting security research.

P1 Security being based in France, read the following extra mentions for more detailed context on the purpose of this software:

DiagNG est un logiciel développé à des fins de sécurité informatique et de recherche, au titre de l'article L122-6-1 du Code de la propriété intellectuelle modifié par l'article 25 de la Loi n° 2013-1168 du 18 décembre 2013 relative à la programmation militaire pour les années 2014 à 2019 et portant diverses dispositions concernant la défense et la sécurité nationale.

DiagNG est également développé en connaissance de l'avis du Conseil d'État, 10ème et 9ème sous-sections réunies, 16/07/2008, 301843, rendu sur saisine de l'APRIL, qui stipule que l'article L122-6-1 du Code de la propriété intellectuelle instaure bien une exception de décompilation destinée à permettre le développement de logiciels libres.


## Development environment setup

Dependencies on Ubuntu 26.04 LTS:

```bash
sudo apt install libgirepository-2.0-dev libadwaita-1-dev \
    gir1.2-modemmanager-1.0 gir1.2-adw-1 gir1.2-gtk-4.0 \
    gir1.2-gtksource-5 libgtksourceview-5-dev \
    python3-dev blueprint-compiler cargo rustc polkitd
```

Dependencies on Archlinux:

```bash
sudo pacman -S uv blueprint-compiler python-gobject \
    gtksourceview5 libadwaita libmm-glib rust polkit
```

Then:

```bash
sudo snap install --classic astral-uv
sudo apt install git
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

## Run project tests

```bash
uv run pytest
```

## Test decoder using KSV

Example command for using [`kaitai_struct_visualizer`](https://github.com/kaitai-io/kaitai_struct_visualizer):

```bash
sudo gem install kaitai-struct-visualizer

ksv \
  ~/qcsuper-dlf-samples/sample_name.dlf \
  ~/diagng/struct/qualcomm/dlf/dlf_file.ksy
```

## Technical architecture

DiagNG is meant to be split into two components:

* `com.p1security.diagng`: The main, single-instance Python 3/GTK 4/libadwaita 1.8+ front process holding a GUI, providing D-Bus session bus IPC on `/com/p1security/diagng` (including the `com.p1security.diagmetad` D-Bus interface which provides info about Linux ModemManager communication, UDev data acquisition)
* `com.p1security.diagmond`: The background, privileged (runs on system bus), single-instance Rust/async process handling raw USB/SPI, USB, Diag frag acquisition, providing IPC
  * Use tokio + `zbus` + [`nusb`](https://github.com/kevinmehall/nusb)?
* Diag frame decoding itself should be done somewhere?

This draft repository (previously called `qcsuper-gui`/QCSuper v3) hence intends to produce a modular GObject+GTK-4 UI app (leveraging GObject data models and signals, and eventually think to make a decoupled UI-daemon thing so that we can perform serial port acquisition in a privileged fashion and the UI and Diag decoder can be unprivileged/sandboxed too) allowing to control and manage interferences with the serial Diag port system wide.

It shares code with `citsued`.

Next tasks are being tracked here: https://github.com/P1sec/DiagNG/issues

We are putting the parsed information in a GObject model and display it using a simple Adwaita UI.

We should maybe eventually try to see how we can interface more with the ModemManager, systemd etc. DBus APIs to handle this more cleany?

Cf. **https://modemmanager.org/docs/modemmanager/port-and-device-detection/**

Cf. https://manpages.debian.org/unstable/modemmanager/mmcli.1.en.html

