#!/usr/bin/env python3

# WIP 2026-05-31: ⚠️
# TODO create a subset of the modemmanager.py script from citsued
# calling DBus in order to scan open devices + PID

# For now this has been copy-pasted from citsued, eventually we should
# convert the calls to HttpWsServer into calls to ServiceRPCClient
# to make it functional (the places with this needs have been
# marked with the "TO BE IMPLEMENTED" comment)

# Also convert some synchronous method calls into asynchronous ones?

# We should use refs to ServiceRPCClient for replying to RPC calls
# from main process with rpc.reply_async(id, gvariant, ...) or send
# calls to main process with rpc.call_async(method, gvariant, ...)
# for every relevant client in ServiceApplication.port_to_client
# (use pubsub patterns/a broadcast method?)


from typing import List, Optional, Dict, Union
from logging import debug, info, warning, error
from subprocess import Popen, DEVNULL, run
from traceback import format_exc
from os import kill, setpgrp
from os.path import realpath
from signal import SIGINT
from json import dumps

from citsued.database.apnlist import ApnList

import gi

gi.require_version('ModemManager', '1.0')
from gi.repository import Gio, GLib, GObject, ModemManager


"""
    This file contains the main code for interfacing
    with the ModemManager DBus interface.

        See: http://wiki.dmz.intl.p1sec.io/index.php/ModemManager_DBus_API
"""


class PinUnlockWaiter:
    WAIT_TIME = 2 * 60  # seconds, avg 30 seconds are needed

    rpc: 'ServiceRPCClient'
    timer: GLib.Source
    timer_soon: GLib.Source
    waiter: Gio.Cancellable
    saved_signal: int

    has_puk: bool
    modem_imei: str  # Used to search for the modem in the actualized state

    saved_unlock_attempts: str = None  # Used to check for changes in
    # attempt count - using an ordered json.dumps output
    modem_is_unlocked: bool = False
    unlock_counts_changed: bool = False

    intf: 'ModemManagerIntf'

    def __init__(
        self,
        intf: 'ModemManagerIntf',
        rpc: 'ServiceRPCClient',
        modem_imei: str,
        pin: str,
        optional_puk: str = None,
    ):

        self.modem_imei = modem_imei
        self.intf = intf
        self.rpc = rpc

        self.has_puk = bool(optional_puk)

        # This should initally set:
        # self.saved_unlock_attempts
        # self.modem_is_unlocked
        # self.unlock_counts_changed
        self.check_modem_unlock_state()
        if self.modem_is_unlocked:
            return self.end()

        # We call here:
        #   citsued.http.utils.HttpUtilsMixin._modem_generic_op
        #    ^ we'll reuse this, but set a custom callback, like in
        #      in citsued.http.modemmanager.HttpModemManagerViews.at_command_cb /
        #         citsued.http.modemmanager.HttpModemManagerViews.at_command_finish
        # Which will not call in turn:
        #   citsued.http.utils.HttpUtilsMixin._generic_op_complete
        #   instead, it will call our callback

        if not self.has_puk:
            # TO BE IMPLEMENTED
            self.cmd_waiter = self.rpc._modem_generic_op(
                self.modem_imei,
                ModemManager.Sim.send_pin,
                self.initial_command_done_cb,
                args=(pin,),
                is_sim=True,
                custom_callback=True,
            )

        else:
            # TO BE IMPLEMENTED
            self.cmd_waiter = self.rpc._modem_generic_op(
                self.modem_imei,
                ModemManager.Sim.send_puk,
                self.initial_command_done_cb,
                args=(optional_puk, pin),
                is_sim=True,
                custom_callback=True,
            )

        if not self.cmd_waiter:
            # The wrong IMSI has been provided and the
            # request has already been cancelled
            return

        # - Wait for the modem to reboot (up to 3 minutes?),
        #   and for the modem to be actually available
        #
        # - Create a signal declaration in citsued.system.networkmanager
        #   or modemmanager for modem (un)lock status availbility change

        self.timer = GLib.timeout_source_new_seconds(self.WAIT_TIME)
        self.timer.set_callback(self.timer_cb)
        self.timer.attach(None)

        self.saved_signal = self.intf.connect(
            'modem_state_change', self.modem_state_changed_cb
        )  # (set state change callback in system.modem_manager)

    def initial_command_done_cb(
        self, sim: ModemManager.Sim, result: Gio.AsyncResult
    ):

        if not self.has_puk:
            finish_method = ModemManager.Sim.send_pin_finish
            finish_method_name = 'ModemManager.Sim.send_pin_finish'
        else:
            finish_method = ModemManager.Sim.send_puk_finish
            finish_method_name = 'ModemManager.Sim.send_puk_finish'

        try:
            return_value = finish_method(sim, result)
        except gi.repository.GLib.GError as err:
            error(finish_method_name + ' error: ' + format_exc())
        else:
            info(
                'Calling %s() on %s returned %s'
                % (
                    finish_method_name,
                    sim.get_object_path(),
                    'OK' if return_value else 'NOK',
                )
            )

        self.check_modem_unlock_state()
        if self.modem_is_unlocked or self.unlock_counts_changed:
            self.end()
        else:
            self.timer_soon = GLib.timeout_source_new_seconds(3)
            self.timer_soon.set_callback(self.timer_soon_cb)
            self.timer_soon.attach(None)

    def check_modem_unlock_state(self, refresh=True):
        if refresh:
            self.intf.update_json_state()

        modems = self.intf.json_state['modems']
        for modem in modems:
            if modem['imei'] == self.modem_imei:
                deep_obj = modem['unlock_retries']
                if deep_obj:
                    # Update self.saved_unlock_attempts:
                    total_count = sum(lock['count'] for lock in deep_obj)

                    if (
                        self.saved_unlock_attempts
                        and total_count < self.saved_unlock_attempts
                    ):
                        self.unlock_counts_changed = True
                    self.saved_unlock_attempts = total_count
                if modem['state']['short_name'] in (
                    'enabled',
                    'registered',
                    'connected',
                ):
                    # Update self.modem_is_unlocked:
                    self.modem_is_unlocked = True
                break
        else:
            return  # Modem not found

    def timer_cb(self, *args):
        self.check_modem_unlock_state()
        self.end()
        return GLib.SOURCE_REMOVE

    def timer_soon_cb(self, *args):
        self.check_modem_unlock_state()
        if self.modem_is_unlocked or self.unlock_counts_changed:
            self.end()
            return GLib.SOURCE_REMOVE
        else:
            return GLib.SOURCE_CONTINUE

    def modem_state_changed_cb(self, *args):
        self.check_modem_unlock_state(refresh=False)
        if self.modem_is_unlocked or self.unlock_counts_changed:
            self.end()

    def end(self):

        if self.timer:
            self.timer.destroy()
        if self.timer_soon:
            self.timer_soon.destroy()
        if self.cmd_waiter:
            self.cmd_waiter.cancel()
        if self.saved_signal:
            self.intf.disconnect(self.saved_signal)

        self.timer = self.timer_soon = None
        self.cmd_waiter = self.saved_signal = None

        # If the HTTP request was interrupted by
        # HttpUtilsMixin._modem_generic_op, as
        # HttpUtilsMixin._generic_op_complete was
        # not called:

        # TO BE IMPLEMENTED
        if self.modem_is_unlocked:
            self.rpc._send_text('OK\n')
        else:
            self.rpc.set_status(500)
            self.rpc.set_response('text/plain', b'NOK\n')

        return GLib.SOURCE_REMOVE


class ModemManagerIntf(GObject.Object):
    state_update_pending: bool = False

    modem_signal_ids: Dict[
        int, object
    ]  # This maps a GLib signal ID to an originating object
    mm_pid: Optional[int] = None
    is_debug_mode: Optional[bool] = None
    needs_relaunch_mm: bool = False
    daemon_connected: bool = False
    rpc: 'ServiceRPCClient' = None
    json_state: Optional[List[dict]] = None
    system_bus: Gio.DBusConnection
    manager: ModemManager.Manager

    def __init__(self):
        super().__init__()

        self.state_update_pending = False

        # Maybe we should use more asynchronicity later?

        self.system_bus = Gio.bus_get_sync(Gio.BusType.SYSTEM, None)
        self.manager = ModemManager.Manager.new_sync(
            self.system_bus,
            Gio.DBusObjectManagerClientFlags.DO_NOT_AUTO_START,
            None,
        )

        # ^ The auto-start directive seems to launch the daemon well
        # on Ubuntu but not on Debian.

        self.manager.connect('notify::name-owner', self.on_daemon_state_change)

        if not self.check_daemon_running():
            self.kill_daemon_and_relaunch()

        self.modem_signal_ids = {}

        self.on_daemon_state_change()

    def check_daemon_running(self):
        """
        Check if a daemon running in --debug mode is
        running on the system.

            returns: (bool) True if an appropriate
            daemon is running
        """

        dbus_proxy = Gio.DBusProxy.new_sync(
            self.system_bus,
            Gio.DBusProxyFlags.NONE,
            None,
            'org.freedesktop.DBus',
            '/org/freedesktop/DBus',
            'org.freedesktop.DBus',
            None,
        )

        try:
            pid = int(
                dbus_proxy.GetConnectionUnixProcessID(
                    '(s)', 'org.freedesktop.ModemManager1'
                )
            )
        except gi.repository.GLib.GError:
            info('No ModemManager service on the system at the moment')
            self.mm_pid = None
            self.is_debug_mode = None
            return False
        else:
            binary_path = realpath('/proc/%s/exe' % pid)
            with open('/proc/%s/cmdline' % pid) as fd:
                args = fd.read().rstrip('\0').split('\0')
            self.is_debug_mode = '--debug' in args
            if self.mm_pid != pid:
                info(
                    '"%s" (pid %s) running on the system'
                    % (' '.join(args), pid)
                )
                self.mm_pid = pid
            return self.is_debug_mode

    def kill_daemon_and_relaunch(self):
        if self.mm_pid is not None:
            warning(
                (
                    'Killing existing daemon (pid %s), it '
                    + 'should be relaunched in debug mode'
                )
                % self.mm_pid
            )

            run(
                ['systemctl', 'stop', 'ModemManager'],
                stdin=DEVNULL,
                stdout=DEVNULL,
                stderr=DEVNULL,
            )
            try:
                kill(self.mm_pid, SIGINT)
            except Exception:
                pass
        self.needs_relaunch_mm = True

    def launch_daemon(self):
        process = Popen(
            ['ModemManager', '--debug'],
            preexec_fn=setpgrp,
            stdin=DEVNULL,
            stdout=DEVNULL,
            stderr=DEVNULL,
        )
        info(
            'Launched the ModemManager daemon in the background in debug mode as pid %s...'
            % (process.pid)
        )

    def find_bearer_by_id(
        self, bearer_id: str
    ) -> Optional[ModemManager.Bearer]:
        bearer_id = int(bearer_id)

        for obj in self.manager.get_objects():
            modem = obj.get_modem()

            for bearer in modem.list_bearers_sync(None):
                path = bearer.get_path()

                if bearer_id == int(path.split('/').pop()):
                    return bearer

    def find_by_imei(self, match_imei: str) -> Optional[ModemManager.Modem]:
        for obj in self.manager.get_objects():
            modem = obj.get_modem()
            modem_imei = modem.get_equipment_identifier()

            if modem_imei == match_imei:
                return modem

    def register_rpc(self, rpc: 'ServiceRPCClient'):
        self.rpc = rpc

    @GObject.Signal
    def modem_state_change(self):
        pass

    def on_daemon_state_change(self, *args):

        if self.manager.get_name_owner():  # Is the daemon currently alive?
            info(
                'ModemManager daemon %s connected.'
                % self.manager.get_version()
            )
            self.daemon_connected = True
            self.modem_signal_ids[
                self.manager.connect('object-added', self.on_modem_added)
            ] = self.manager
            self.modem_signal_ids[
                self.manager.connect('object-removed', self.on_modem_removed)
            ] = self.manager
            # Loop to connect all modem signals, and add these to self.modem_signal_ids
            for obj in self.manager.get_objects():
                modem = obj.get_modem()
                self.modem_signal_ids[
                    modem.connect('state-changed', self.on_modem_state_updated)
                ] = modem
        else:
            error('ModemManager daemon disconnected.')
            self.daemon_connected = False
            # Disconnect/discard from the Python set structure all
            # signals from self.modem_signal_ids
            for signal_id, obj in sorted(self.modem_signal_ids.items()):
                obj.disconnect(
                    signal_id
                )  # See https://lazka.github.io/pgi-docs/GObject-2.0/classes/Object.html#GObject.Object.disconnect
            self.modem_signal_ids = {}

            if self.needs_relaunch_mm:
                self.launch_daemon()
                self.needs_relaunch_mm = False

        self.queue_state_update()

    def queue_state_update(self):
        if not self.state_update_pending:
            self.state_update_pending = True
            GLib.idle_add(self.update_json_state)

    def update_json_state(self, *args):

        self.json_state = self.dbus_metadata_to_json(self.manager)

        debug('ModemManager info: ' + dumps(self.json_state, indent=4))

        if self.rpc:
            # TO BE IMPLEMENTED
            self.rpc.broadcast_message(
                {'type': 'SYNC_MODEM_STATUS', **self.json_state}
            )

        self.emit('modem_state_change')

        self.state_update_pending = False

    def on_modem_added(self, manager, obj):
        modem = obj.get_modem()
        # Log this better maybe?
        info(
            '[ModemWatcher] %s: modem managed by ModemManager [%s]: %s (%s)'
            % (
                obj.get_object_path(),
                modem.get_equipment_identifier(),
                modem.get_manufacturer(),
                modem.get_model(),
            )
        )

        self.modem_signal_ids[
            modem.connect('state-changed', self.on_modem_state_updated)
        ] = modem

        self.queue_state_update()

    def on_modem_removed(self, manager, obj):
        info(
            '[ModemWatcher] %s: modem unmanaged by ModemManager'
            % obj.get_object_path()
        )

        self.queue_state_update()

    def on_modem_state_updated(self, modem, old, new, reason):
        info(
            '[ModemWatcher] %s: modem state updated: %s -> %s (%s) '
            % (
                modem.get_object_path(),
                ModemManager.ModemState.get_string(old),
                ModemManager.ModemState.get_string(new),
                ModemManager.ModemStateChangeReason.get_string(reason),
            )
        )

        self.queue_state_update()

    def sim_to_dict(self, sim: ModemManager.Sim) -> dict:

        gid1 = sim.get_gid1()
        gid2 = sim.get_gid2()

        mcc_mnc: Optional[str] = sim.get_operator_identifier()
        suggested_apns = None
        if mcc_mnc:
            mcc = mcc_mnc[:3]
            mnc = mcc_mnc[3:]  # May contain a leading 0

            suggested_apns = ApnList.get_suggested_apns(mcc, mnc)

        return (
            {
                'path': sim.get_path(),  # str
                'iccid': sim.get_identifier(),  # str
                'imsi': sim.get_imsi(),  # str or None if unknown
                'eid': sim.get_eid(),  # str if an eSIM or None
                'gid1': gid1.hex() if gid1 else None,  # str or None
                'gid2': gid2.hex() if gid2 else None,  # str or None
                'is_active': sim.get_active(),  # bool
                'is_removable': sim.get_removability(),  # ModemManager.SimRemovability
                'emergency_numbers': sim.get_emergency_numbers(),  # list of strs
                'operator_identifier': mcc_mnc,  # str or None
                'operator_name': sim.get_operator_name(),  # str or None,
                'apns_by_operator': suggested_apns,  # List[Dict[str, object]] or None
                'sim_type': sim.get_sim_type(),  # ModemManager.SimType
            }
            if sim
            else None
        )

    def _use_none(self, number: Union[int, float]):
        if number in (GObject.G_MAXUINT, -GObject.G_MAXDOUBLE):
            return None
        return number

    def cell_to_dict(self, cell: ModemManager.CellInfo) -> dict:

        data = {
            'cell_type': cell.get_cell_type(),
            'is_serving': cell.get_serving(),
        }

        if isinstance(cell, ModemManager.CellInfoGsm):
            data.update(
                {
                    'arfcn': self._use_none(
                        cell.get_arfcn()
                    ),  # int or GObject.G_MAXUINT
                    'base_station_id': cell.get_base_station_id(),  # str or None
                    'cell_identifier': cell.get_ci(),  # str or None
                    'location_area': cell.get_lac(),  # str or None
                    'mcc_mnc': cell.get_operator_id(),  # str or None
                    'rx_level': self._use_none(
                        cell.get_rx_level()
                    ),  # int or GObject.G_MAXUINT
                    'timing_advance': self._use_none(
                        cell.get_timing_advance()
                    ),  # int or GObject.G_MAXUINT
                }
            )

        elif isinstance(cell, ModemManager.CellInfoUmts):
            data.update(
                {
                    'cell_identifier': cell.get_ci(),  # str or None
                    'ecio': self._use_none(
                        cell.get_ecio()
                    ),  # float or -GObject.G_MAXDOUBLE
                    'frequency_fdd_dl': self._use_none(
                        cell.get_frequency_fdd_dl()
                    ),  # int or GObject.G_MAXUINT
                    'frequency_fdd_ul': self._use_none(
                        cell.get_frequency_fdd_ul()
                    ),  # int or GObject.G_MAXUINT
                    'frequency_tdd': self._use_none(
                        cell.get_frequency_tdd()
                    ),  # int or GObject.G_MAXUINT
                    'location_area': cell.get_lac(),  # str or None
                    'mcc_mnc': cell.get_operator_id(),  # str or None
                    'path_loss': self._use_none(
                        cell.get_path_loss()
                    ),  # int or GObject.G_MAXUINT
                    'psc': self._use_none(
                        cell.get_psc()
                    ),  # int or GObject.G_MAXUINT
                    'rpsc': self._use_none(
                        cell.get_rspc()
                    ),  # float or -GObject.G_MAXDOUBLE
                    'uarfcn': self._use_none(
                        cell.get_uarfcn()
                    ),  # int or GObject.G_MAXUINT
                }
            )

        elif isinstance(cell, ModemManager.CellInfoLte):
            data.update(
                {
                    'bandwidth': self._use_none(
                        cell.get_bandwidth()
                    ),  # int or GObject.G_MAXUINT
                    'cell_identifier': cell.get_ci(),  # str or None
                    'earfcn': self._use_none(
                        cell.get_earfcn()
                    ),  # int or GObject.G_MAXUINT
                    'mcc_mnc': cell.get_operator_id(),  # str or None
                    'physical_ci': cell.get_physical_ci(),  # str or None
                    'rsrp': self._use_none(
                        cell.get_rsrp()
                    ),  # float or -GObject.G_MAXDOUBLE
                    'rsrq': self._use_none(
                        cell.get_rsrq()
                    ),  # float or -GObject.G_MAXDOUBLE
                    'serving_cell_type': cell.get_serving_cell_type(),  # GEnum
                    'tac': cell.get_tac(),  # str
                    'timing_advance': self._use_none(
                        cell.get_timing_advance()
                    ),  # int or GObject.G_MAXUINT
                }
            )

        elif isinstance(cell, ModemManager.CellInfoNr5g):
            data.update(
                {
                    'bandwidth': self._use_none(
                        cell.get_bandwidth()
                    ),  # int or GObject.G_MAXUINT
                    'cell_identifier': cell.get_ci(),  # str or None
                    'nrarfcn': self._use_none(
                        cell.get_nrarfcn()
                    ),  # int or GObject.G_MAXUINT
                    'mcc_mnc': cell.get_operator_id(),  # str or None
                    'physical_ci': cell.get_physical_ci(),  # str or None
                    'rsrp': self._use_none(
                        cell.get_rsrp()
                    ),  # float or -GObject.G_MAXDOUBLE
                    'rsrq': self._use_none(
                        cell.get_rsrq()
                    ),  # float or -GObject.G_MAXDOUBLE
                    'serving_cell_type': cell.get_serving_cell_type(),  # GEnum
                    'sinr': self._use_none(
                        cell.get_sinr()
                    ),  # float or -GObject.G_MAXDOUBLE
                    'tac': cell.get_tac(),  # str
                    'timing_advance': self._use_none(
                        cell.get_timing_advance()
                    ),  # int or GObject.G_MAXUINT
                }
            )

        else:
            pass  # TODO decode other cell types, including TDMA?

        return data

    def bearer_ipconfig_to_dict(self, cfg: ModemManager.BearerIpConfig):

        return (
            {
                'address': cfg.get_address(),  # str or None
                'dns': cfg.get_dns(),  # list of strings and None
                'gateway': cfg.get_gateway(),  # str or None
                'method': cfg.get_method(),  # GEnum - ModemManager.BearerIpMethod
                'mtu': cfg.get_mtu(),  # int
                'prefix': cfg.get_prefix(),  # int
            }
            if cfg
            else None
        )

    def bearer_properties_to_dict(self, props: ModemManager.BearerProperties):

        return (
            {
                'access_type_preference': props.get_access_type_preference(),  # GEnum - ModemManager.BearerAccessTypePreference
                'allow_roaming': props.get_allow_roaming(),  # bool
                'allowed_auth': props.get_allowed_auth(),  # GFlags - ModemManager.BearerAllowedAuth
                'apn': props.get_apn(),  # str
                'apn_type': props.get_apn_type(),  # GFlags - BearerApnType
                'ip_type': props.get_ip_type(),  # GFlags - BearerIpFamily
                'multiplex': props.get_multiplex(),  # GEnum - BearerMultiplexSupport
                'number': props.get_number(),  # str
                'password': props.get_password(),  # str
                'profile_id': props.get_profile_id(),  # int
                'profile_name': props.get_profile_name(),  # str
                'rm_protocol': props.get_rm_protocol(),  # GEnum - ModemManager.ModemCdmaRmProtocol
                'roaming_allowance': props.get_roaming_allowance(),  # GFlags - ModemManager.BearerRoamingAllowance
                'user': props.get_user(),  # str
            }
            if props
            else None
        )

    def bearer_stats_to_dict(self, stats: ModemManager.BearerStats):

        return {
            'attempts': stats.get_attempts(),  # int
            'failed_attempts': stats.get_failed_attempts(),  # int
            'start_date': stats.get_start_date(),  # int
            'duration_seconds': stats.get_duration(),  # int
            'total_duration': stats.get_total_duration(),  # int
            'downlink_speed_bps': stats.get_downlink_speed(),  # int
            'uplink_speed_bps': stats.get_uplink_speed(),  # int
            'rx_bytes': stats.get_rx_bytes(),  # int
            'total_rx_bytes': stats.get_total_rx_bytes(),  # int
            'tx_bytes': stats.get_tx_bytes(),  # int
            'total_tx_bytes': stats.get_total_tx_bytes(),  # int
        }

    def bearer_to_dict(self, bearer: ModemManager.Bearer) -> dict:

        connection_error = bearer.get_connection_error()
        if connection_error:
            connection_error = repr(connection_error)

        return {
            'path': bearer.get_path(),  # str
            'interface': bearer.get_interface(),  # str
            'bearer_type': bearer.get_bearer_type(),  # GEnum - ModemManager.BearerType
            'is_connected': bearer.get_connected(),  # bool
            'connection_error': connection_error,  # str or None
            'ip_timeout': bearer.get_ip_timeout(),  # int
            'ipv4_config': self.bearer_ipconfig_to_dict(
                bearer.get_ipv4_config()
            ),  # dict or None
            'ipv6_config': self.bearer_ipconfig_to_dict(
                bearer.get_ipv6_config()
            ),  # dict or None
            'is_multiplexed': bearer.get_multiplexed(),  # bool
            'profile_id': bearer.get_profile_id(),  # int
            'properties': self.bearer_properties_to_dict(
                bearer.get_properties()
            ),  # dict or None
            'reload_stats_supported': bearer.get_reload_stats_supported(),  # bool
            'stats': self.bearer_stats_to_dict(
                bearer.get_stats()
            ),  # dict or None
            'suspended': bearer.get_suspended(),  # bool
        }

    def dbus_metadata_to_json(self, manager: ModemManager.Manager) -> dict:
        # Avoid memory leaks?

        output = []

        for obj in manager.get_objects():
            modem = obj.get_modem()
            unlock_retries = []
            modem.peek_unlock_retries().foreach(
                lambda lock, count, *ud: unlock_retries.append(
                    {'lock': lock, 'count': count}
                ),
                None,
            )

            # For all available information retrieval methods, see:
            # https://lazka.github.io/pgi-docs/ModemManager-1.0/classes/Modem.html
            # https://lazka.github.io/pgi-docs/ModemManager-1.0/classes/Sim.html

            try:
                sim_maybe = modem.get_sim_sync(None)
            except gi.repository.GLib.GError:
                sim_maybe = None

            try:
                sim_slots = modem.get_sim_slot_paths()
            except gi.repository.GLib.GError:
                sim_slots = None

            try:
                cell_info = modem.get_cell_info_sync(None)
                if cell_info:
                    cell_info = [self.cell_to_dict(cell) for cell in cell_info]
            except gi.repository.GLib.GError:
                cell_info = None

            signal_quality: Optional[int] = None
            signal_quality_recent: Optional[bool] = None
            try:
                quality_info = modem.get_signal_quality()
                if quality_info:
                    signal_quality, signal_quality_recent = quality_info
            except gi.repository.GLib.GError:
                pass

            # TODO: Use Modem.ModemSignal.setup instead of doing this

            # TODO: Make the functions above properly async ^

            supported_modes = modem.get_supported_modes()
            # if supported_modes[0]:
            #     supported_modes = [mode for mode in supported_modes[1]
            #         if mode.preferred]

            output.append(
                self.visit_gobj_to_json(
                    {
                        'path': modem.dup_path(),
                        'imei': modem.get_equipment_identifier(),
                        'state': modem.get_state(),
                        'power_state': modem.get_power_state(),
                        'state_failed_reason': modem.get_state_failed_reason(),
                        'unlock_required': modem.get_unlock_required(),
                        'unlock_retries': unlock_retries,
                        'manufacturer': modem.get_manufacturer(),  # str
                        'model': modem.get_model(),  # str
                        'plugin': modem.get_plugin(),  # str
                        'revision': modem.get_revision(),  # str
                        'physical_device': modem.get_device(),  # str
                        'primary_port': modem.get_primary_port(),  # str
                        'unique_id': modem.get_device_identifier(),  # str
                        'drivers': modem.get_drivers(),  # list of str
                        'hardware_revision': modem.get_hardware_revision(),  # str
                        'ports': modem.get_ports(),  # list of dicts # peek instead ?
                        # Mostly not useful or void:
                        'carrier_configuration': modem.get_carrier_configuration(),
                        'carrier_configuration_revision': modem.get_carrier_configuration_revision(),
                        'cell_info': cell_info,
                        'signal_quality': signal_quality,
                        'signal_quality_recent': signal_quality_recent,
                        'access_technologies': modem.get_access_technologies(),
                        'supported_ip_families': modem.get_supported_ip_families(),
                        'supported_modes': supported_modes,
                        'supported_capabilities': modem.get_supported_capabilities(),  # peek ?
                        'supported_bands': modem.get_supported_bands(),
                        'current_capabilities': modem.get_current_capabilities(),
                        'current_modes': modem.get_current_modes(),
                        'current_bands': modem.get_current_bands(),
                        'current_sim': (
                            self.sim_to_dict(sim_maybe) if sim_maybe else None
                        ),  # dict, see self.sim_to_dict that will be called
                        'primary_sim_slot': modem.get_primary_sim_slot(),  # int - bad value sometimes
                        'sim_slots': sim_slots,  # list of dicts or None - bad value sometimes
                        'bearers': list(
                            map(
                                self.bearer_to_dict,
                                modem.list_bearers_sync(None),
                            )
                        ),
                    }
                )
            )

        self.check_daemon_running()

        return {
            'is_running': self.mm_pid is not None,
            'pid': self.mm_pid,
            'version': self.manager.get_version(),
            'has_debug_flag': self.is_debug_mode,
            'modems': output,
        }

    """
        Recursively serialize the GDBus-returned values into usable
        JSON (visitor pattern).

            :param value (str): Value to serialize
            :return: The converted value
    """

    def visit_gobj_to_json(self, value: object) -> object:
        """
        dict => dict (visit values)
        list => list (visit members)
        int => int
        str => str
        NoneType, bool, anything else unhandled => same literal
        isinstance(x, gi._gi.ResultTuple) => [1]

        isinstance(x, GObject.GEnum)
            =>
                NOT?
                value_name (.value_name)
                value_nick (.value_nick)
                value (.__int__())
                type_name (.__gtype__.name)

                BUT JUST?
                long_name: .__gtype__.name + '.' + .value_name
                short_name: .value_nick

        isinstance(x, GObject.GFlags)
                zip(.value_names, .value_nicks) => (value_name, value_nick)
                    long_name: .__gtype__.name + '.' + value_name
                    short_name: value_nick

        isinstance(x, gi._gi.Struct)
            Get the first field value:
                getattr(x, x.__info__.get_fields()[0].get_name())

        """

        if isinstance(value, gi._gi.ResultTuple):
            return self.visit_gobj_to_json(value[1])
        elif isinstance(value, GObject.GEnum):
            return {
                'long_name': value.__gtype__.name + '.' + value.value_name,
                'short_name': value.value_nick,
            }
        elif isinstance(value, GObject.GFlags):
            return [
                {
                    'long_name': value.__gtype__.name + '.' + value_name,
                    'short_name': value_nick,
                }
                for value_name, value_nick in zip(
                    value.value_names, value.value_nicks
                )
            ]
        elif isinstance(value, gi._gi.Struct):
            return {
                field.get_name(): self.visit_gobj_to_json(
                    getattr(value, field.get_name(), None)
                )
                for field in value.__info__.get_fields()
            }
        elif isinstance(value, dict):
            return {
                key: self.visit_gobj_to_json(val) for key, val in value.items()
            }
        elif isinstance(value, list) or isinstance(value, tuple):
            return [self.visit_gobj_to_json(member) for member in value]
        else:
            return value
