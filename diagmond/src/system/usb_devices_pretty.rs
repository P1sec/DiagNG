use crate::system::usb_devices::UsbDevicesEndpointResp;

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbDeviceNodePretty {
    description: String,
    original_json: String,
    children: Vec<Self>,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbDeviceTreePretty {
    devices: Vec<UsbDeviceNodePretty>,
}

pub fn device_tree_to_pretty(data: UsbDevicesEndpointResp) -> UsbDeviceTreePretty {
    let mut output = UsbDeviceTreePretty { devices: vec![] };

    // WIP find a way to keep self.device_list ListStore
    // complete + synced with nusb/crate::usb_polled::UsbDevicesEndpointResp data...
    // Cf. https://gtk-rs.org/gtk-rs-core/git/docs/gio/struct.ListStore.html#method.find_with_equal_func
    // Cf. https://gtk-rs.org/gtk-rs-core/git/docs/gio/struct.ListStore.html#method.retain

    if let Some(device_tree) = data.device_tree {
        for bus in device_tree.0 {
            // if usb_bus.devices.len() > 0 { // Ignore empty buses
            let mut bus_entry = UsbDeviceNodePretty {
                description: glib::markup_escape_text(&format!("{}", bus)).to_string(),
                original_json: serde_json::to_string_pretty(&bus).unwrap(),
                children: vec![],
            };

            for device in bus.devices {
                let mut device_entry = UsbDeviceNodePretty {
                    description: device.get_markup(),
                    original_json: serde_json::to_string_pretty(&device).unwrap(),
                    children: vec![],
                };

                for configuration in device.configurations {
                    let mut configuration_entry = UsbDeviceNodePretty {
                        description: glib::markup_escape_text(&format!("{}", configuration))
                            .to_string(),
                        original_json: serde_json::to_string_pretty(&configuration).unwrap(),
                        children: vec![],
                    };

                    for interface in configuration.interfaces {
                        if let Some(ref alt_settings) = interface.alt_settings {
                            let has_alt_settings = alt_settings.len() > 1;

                            for alt_setting in alt_settings {
                                let mut interface_string = interface.get_markup();
                                if has_alt_settings {
                                    interface_string +=
                                        format!(" (alt_setting={})", alt_setting.b_alt_setting)
                                            .as_str();
                                }

                                let mut interface_entry = UsbDeviceNodePretty {
                                    description: interface_string,
                                    original_json: serde_json::to_string_pretty(&interface)
                                        .unwrap(),
                                    children: vec![],
                                };

                                // obj.device_tree_model().unwrap().set_autoexpand(false);
                                for endpoint in &alt_setting.endpoints {
                                    let endpoint_entry = UsbDeviceNodePretty {
                                        description: format!("{}", endpoint),
                                        original_json: serde_json::to_string_pretty(&endpoint)
                                            .unwrap(),
                                        children: vec![],
                                    };
                                    interface_entry.children.push(endpoint_entry);
                                }
                                // obj.device_tree_model().unwrap().set_autoexpand(true);

                                configuration_entry.children.push(interface_entry);
                            }
                        } else {
                            let interface_entry = UsbDeviceNodePretty {
                                description: interface.get_markup(),
                                original_json: serde_json::to_string_pretty(&interface).unwrap(),
                                children: vec![],
                            };

                            configuration_entry.children.push(interface_entry);
                        }
                    }

                    device_entry.children.push(configuration_entry);
                }

                bus_entry.children.push(device_entry);
            }

            output.devices.push(bus_entry);
            // }
        }
    }

    output
}
