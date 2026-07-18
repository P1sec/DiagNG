# `com.p1security.diagng`

This folder contains a Flatpak template for the https://github.com/P1sec/DiagNG GUI

## Local build instructions

## Build instructions

Build dependencies:

```
sudo apt install flatpak-builder flatpak build-essential \
    libgirepository-2.0-dev libadwaita-1-dev \
    gir1.2-modemmanager-1.0 gir1.2-adw-1 gir1.2-gtk-4.0 \
    gir1.2-gtksource-5 libgtksourceview-5-dev \
    python3-dev python3-pip blueprint-compiler \
    appstream git
sudo snap install --classic astral-uv
```

Then, run:

```
./build.sh
```

## Utilities

These command will generate a `python3-modules.json` file that can serve as a template for specifying the dependencies into `com.p1security.diagng.json`:

```bash
cd
git clone git@github.com:flatpak/flatpak-builder-tools.git
git clone git@github.com:P1sec/DiagNG.git diagng

cd ~/flatpak-builder-tools/pip
uv sync --all-groups --frozen
source .venv/bin/activate

cd ~/diagng/packaging/flatpak
~/flatpak-builder-tools/pip/flatpak-pip-generator --pyproject-file ~/diagng/pyproject.toml
```
