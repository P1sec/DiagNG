# TODO

# TODO: This abstract/base class should
# abstract connecting to the ADB daemon
# through the ADBClient class (ONCE OR MORE) +
# sending the "host:transport:${self.device.serial_str}"
# command each time before sending other commands
# on the TCP stream +
# HOLDING A STATE MACHINE (UNSTARTED, PROGRESS, SUCCESS,
# FAILED) + POSSIBLE TEXT RETURN_INFO
