# WIP - Cf. https://docs.gtk.org/gio/class.FileMonitor.html -
#   https://github.com/P1sec/DiagNG/issues/10

#   => https://lazka.github.io/pgi-docs/Gio-2.0/classes/File.html#Gio.File.monitor_directory


class UdevRulesMonitor:
    app: 'MainApplication'

    def __init__(self, app):

        self.app = app

        pass  # WIP
