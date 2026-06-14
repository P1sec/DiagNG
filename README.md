<p align="center">
<img src="https://github.com/P1sec/DiagNG/blob/main/pics/project_banner.png" alt="Landing illustration">
</p>

# DiagNG 🍕 🎧 The next-generation baseband Diag-collecting software (2G/3G/4G)

This software contains a work-in-progress intended sequel (v3) for [QCSuper](https://github.com/P1sec/QCSuper).

It is meant to be split into three components:

* `com.p1security.diagng`: The main, single-instance Python 3/GTK 4/libadwaita front process holding a GUI, providing IPC (currently a DBus lock + JSON-RPC/GVariant interface)
* `com.p1security.diagngd`: The background, unprivileged, single-instance Python3/GObject process handling on Linux ModemManager communication, UDev data acquisition, providing IPC (currently a DBus lock + JSON-RPC/GVariant interface)
* TODO: `com.p1security.diagmond`: The background, privilege-escalatable, single-instance Rust/async process handling raw USB/SPI, USB, Diag frag acquisition, providing IPC
  * Use tokio + [`dbus-rs/dbus-tokio`](https://github.com/diwic/dbus-rs/blob/master/dbus-tokio/examples/tokio_server_cr.rs) (`zbus` is slop) + [`nusb`](https://github.com/kevinmehall/nusb)?
* Diag frame decoding itself should be done somewhere?

This draft repository (previously called `qcsuper-gui`/QCSuper v3) hence intends to produce a modular GObject+GTK-4 UI app (leveraging GObject data models and signals, and eventually think to make a decoupled UI-daemon thing so that we can perform serial port acquisition in a privileged fashion and the UI and Diag decoder can be unprivileged/sandboxed too) allowing to control and manage interferences with the serial Diag port system wide.

It shares code with `citsued`.

Next tasks are being tracked here: https://github.com/P1sec/DiagNG/issues

=> **Put the parsed information in a GObject model and display it using a simple Adwaita UI?**

MAYBE DO LATER: Emulate the behavior of `psutil`/`fuser`, scanning `/proc/*/fd` for symlinks to `/dev/ttyUSB*` and `/dev/ttyHS*` (QCSuper already does this: https://github.com/P1sec/QCSuper/blob/2.1.1/src/qcsuper/inputs/usb_modem_pyserial.py#L106) - Maybe using a regular timeout/background task + root escalation of a forked subprocess? (use PIPE for communication?)

Then, try to see how we can interface more with the ModemManager, systemd etc. DBus APIs to handle this more cleany?

Double check about the ModemManager `InhibitDevice` API (https://www.freedesktop.org/software/ModemManager/api/latest/gdbus-org.freedesktop.ModemManager1.html#gdbus-method-org-freedesktop-ModemManager1.InhibitDevice) + device list + whether any lock mechanism was implemented since we last checked about it (https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/6)?

+ the part interacting with `udev` rules?

Cf. **https://modemmanager.org/docs/modemmanager/port-and-device-detection/**

Cf. https://manpages.debian.org/unstable/modemmanager/mmcli.1.en.html

Use the subprocess spawning process to do privileged stuff? etc.

## Current setup for running the prototype

Dependencies on Ubuntu 26.04 LTS:

```bash
sudo apt install libgirepository-2.0-dev libadwaita-1-dev \
    gir1.2-jsonrpc-1.0 gir1.2-json-1.0 libjsonrpc-glib-1.0-dev \
    gir1.2-modemmanager-1.0 gir1.2-adw-1 gir1.2-gtk-4.0 \
    gir1.2-gtksource-5 libgtksourceview-5-dev \
    python3-dev blueprint-compiler
```

Dependencies on Archlinux:

```bash
sudo pacman -S uv blueprint-compiler python-gobject jsonrpc-glib \
    gtksourceview5 libadwaita libmm-glib
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

diagng
```
