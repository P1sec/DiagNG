#!/usr/bin/env python3

from usb.legacy import busses
from usb.core import _try_get_string


class PyUSBThread:
    # ⚠️ WIP

    def get_pyusb_metadata(self) -> dict:
        # List buses using PyUSB, then reconstruct output compatible with
        # the nusb debug JSON data from diagmond

        out_json = {
            'status': 'OK',
            'error_code': None,
            'error_string': 'None',
            'device_tree': [],
        }

        for bus in busses():
            # print('Bus', '=>', bus.__dict__)
            # print()

            bus_obj = {
                'node_type': 'BUS',
                'bus_string': '%03d' % bus.location,
                'driver_string': None,
                'controller_type': None,
                'readable_name': None,
                'devices': [],
            }
            out_json['device_tree'].append(bus_obj)

            for legacy_device in bus.devices:
                device = legacy_device.dev
                # print('  Device', '=>', legacy_device.__dict__, '/', device.__dict__)
                # print()

                dev_obj = {
                    'node_type': 'DEVICE',
                    'raw_descriptor': None,
                    'class': device.bDeviceClass,
                    'subclass': device.bDeviceSubClass,
                    'protocol': device.bDeviceProtocol,
                    'vendor_id': '%04x' % device.idVendor,
                    'product_id': '%04x' % device.idProduct,
                    'serial_number': None,
                    'bcd_dev_version': legacy_device.deviceVersion.replace(
                        '.', ''
                    ),
                    'bcd_usb_version': legacy_device.usbVersion.replace(
                        '.', ''
                    ),
                    'vendor_name': None,
                    'product_name': None,
                    'speed_mbps': {
                        1: 1.5,
                        2: 12.0,
                        3: 480.0,
                        4: 480.0,
                        5: 5000.0,
                        6: 10000.0,
                    }[device.speed],
                    'speed_type': {
                        1: 'LOW',
                        2: 'FULL',
                        3: 'HIGH',
                        4: 'WIRELESS',
                        5: 'SUPER',
                        6: 'SUPER_PLUS',
                    }[device.speed],
                    'bus_string': '%03d' % bus.location,
                    'port_chain': list(
                        device.port_numbers
                        if device.port_numbers
                        else [device.port_number]
                    ),
                    'can_open': True,
                    'configurations': [],
                }

                try:
                    dev_obj['vendor_name'] = device.manufacturer
                    dev_obj['product_name'] = device.product
                    dev_obj['serial_number'] = device.serial_number
                    active_config = device.get_active_configuration()
                except Exception:
                    dev_obj['can_open'] = False
                    active_config = None

                # help(device) # Test command
                # exit()

                # See: device.detach_kernel_driver (⚠️ PRIVILEGED), device.is_kernel_driver_active(intf)
                # device.set_configuration(XX)
                # device.set_interface_altsetting(XX)
                # device.write(XX)
                # device.default_timeout

                bus_obj['devices'].append(dev_obj)

                for num_configuration, configuration in enumerate(
                    device.configurations()
                ):
                    # print('    Configuration', '=>', configuration.__dict__)

                    cfg_obj = {
                        'is_active': (
                            configuration.iConfiguration
                            == active_config.iConfiguration
                        )
                        if active_config
                        else None,
                        'b_configuration_number': configuration.bConfigurationValue,
                        'i_configuration': _try_get_string(
                            device,
                            configuration.iConfiguration,
                            default_access_error=None,
                        )
                        or None,
                        'bm_attributes': configuration.bmAttributes,
                        'max_power_ma': configuration.bMaxPower,
                        'interfaces': [],
                    }

                    dev_obj['configurations'].append(cfg_obj)

                    for interface in configuration:
                        # print('        Interface', '=>', interface.__dict__)

                        while (
                            len(cfg_obj['interfaces'])
                            < interface.bInterfaceNumber + 1
                        ):
                            cfg_obj['interfaces'].append({})

                        intf_obj = cfg_obj['interfaces'][
                            interface.bInterfaceNumber
                        ]

                        if not intf_obj:
                            intf_obj.update(
                                {
                                    'b_interface_number': interface.bInterfaceNumber,
                                    'i_interface': _try_get_string(
                                        device,
                                        interface.iInterface,
                                        default_access_error=None,
                                    )
                                    or None,
                                    'class': interface.bInterfaceClass,
                                    'subclass': interface.bInterfaceSubClass,
                                    'protocol': interface.bInterfaceProtocol,
                                    'alt_settings': [],
                                }
                            )

                        alt_setting_obj = {
                            'b_alt_setting': interface.bAlternateSetting,
                            'class': interface.bInterfaceClass,
                            'subclass': interface.bInterfaceSubClass,
                            'protocol': interface.bInterfaceProtocol,
                            'endpoints': [],
                        }

                        intf_obj['alt_settings'].append(alt_setting_obj)

                        for endpoint in interface:
                            # print('          Endpoint', '=>', endpoint.__dict__)

                            endpoint_obj = {
                                'b_endpoint_address': endpoint.bEndpointAddress,
                                'bm_attributes': endpoint.bmAttributes,
                                'direction': 'IN'
                                if bool(endpoint.bEndpointAddress & 0x80)
                                else 'OUT',
                                'transfer_type': {
                                    0: 'CONTROL',
                                    1: 'ISOCHRONOUS',
                                    2: 'BULK',
                                    3: 'INTERRUPT',
                                }[endpoint.bmAttributes & 0x03],
                                'bytes_per_packet': endpoint.wMaxPacketSize
                                & ((1 << 11) - 1),
                                'packets_per_microframe': (
                                    (endpoint.wMaxPacketSize >> 11) & 0b11
                                )
                                + 1,
                                'polls_between_microframe': endpoint.bInterval,
                            }

                            alt_setting_obj['endpoints'].append(endpoint_obj)

                    cfg_obj['interfaces'] = list(
                        filter(None, cfg_obj['interfaces'])
                    )

        # print(dumps(out_json, indent=4))

        return out_json
