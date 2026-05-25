WIP: Create a Python module allowing to control and manage interferences with the serial Diag port system-wide.

NEXT STEP: Emulate the behavior of `psutil`/`fuser`, scanning `/proc/*/fds` for symlinks to `/dev/ttyUSB*` and `/dev/ttyHS*`? (Maybe QCSuper already does this?)

Then, try to see how we can interace with the ModemManager, systemd etc. DBus APIs to handle this more cleany?

Double check about the ModemManager `InhibitDevice` API (https://www.freedesktop.org/software/ModemManager/api/latest/gdbus-org.freedesktop.ModemManager1.html#gdbus-method-org-freedesktop-ModemManager1.InhibitDevice) + device list + whether any lock mechanism was implemented since we last checked about it (https://gitlab.freedesktop.org/mobile-broadband/ModemManager/-/merge_requests/6)?

+ the part interacting with `udev` rules?

Cf. **https://modemmanager.org/docs/modemmanager/port-and-device-detection/**

Cf. https://manpages.debian.org/unstable/modemmanager/mmcli.1.en.html

Use the subprocess spawning process to do privileged stuff? etc.
