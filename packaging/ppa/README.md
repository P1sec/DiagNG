The `upload_source_package.sh` script that should be added to this directory should build a signed .DEB source package suitable for uploading to Launchpad PPAs, and upload it automatically. Dependencies for the script include `coreutils`, `dput`, `debhelper`, `dh-python` and `devscripts` + the `stdeb` and `poetry` PyPI packages.

```bash
sudo snap install --classic astral-uv
sudo apt install coreutils dput debhelper dh-python python3-all python3-all-dev devscripts
sudo pip3 install stdeb --break-system-packages
uv tool install poetry

poetry build -f sdist

py2dsc-deb -x stdeb.cfg --suite resolute --sign-results --sign-key 87EC6DB535CC2A084B41E88EF675C22E1B4B2ACC \
    --debian-version 1 ../../dist/diagng-0.1.0.tar.gz
```

Then, to install the remote package:

```bash
sudo add-apt-repository -y ppa:marin-m/qcsuper
sudo apt update
sudo apt install -y diagng
```
