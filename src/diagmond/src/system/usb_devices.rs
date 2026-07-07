use std::collections::HashMap;

#[derive(serde::Serialize, serde::Deserialize)]
pub enum UsbDeviceTreeNodeType {
    BUS,
    DEVICE,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub enum UsbEndpointDirection {
    IN,
    OUT,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub enum UsbEndpointTransferType {
    CONTROL,
    ISOCHRONOUS,
    BULK,
    INTERRUPT,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbEndpoint {
    pub b_endpoint_address: u8,
    bm_attributes: u8,
    pub direction: UsbEndpointDirection,
    pub transfer_type: UsbEndpointTransferType,
    pub bytes_per_packet: usize,
    pub packets_per_microframe: u8,
    pub polls_between_microframe: u8,
}

impl std::fmt::Display for UsbEndpoint {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let mtu_string = if self.packets_per_microframe > 1 {
            format!(
                "{} x {} packets",
                self.bytes_per_packet, self.packets_per_microframe
            )
        } else {
            format!("{}", self.bytes_per_packet)
        };

        let endpoint_string = format!(
            "Endpoint {} - {} - {} (mtu={}, interval={})",
            self.b_endpoint_address,
            match self.direction {
                UsbEndpointDirection::IN => "IN",
                UsbEndpointDirection::OUT => "OUT",
            },
            match self.transfer_type {
                UsbEndpointTransferType::CONTROL => "CONTROL",
                UsbEndpointTransferType::ISOCHRONOUS => "ISOCHRONOUS",
                UsbEndpointTransferType::BULK => "BULK",
                UsbEndpointTransferType::INTERRUPT => "INTERRUPT",
            },
            mtu_string,
            self.polls_between_microframe
        );
        write!(f, "{}", endpoint_string)
    }
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbAltSetting {
    pub b_alt_setting: u8,
    class: u8,
    subclass: u8,
    protocol: u8,
    pub endpoints: Vec<UsbEndpoint>,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbInterface {
    pub b_interface_number: u8,
    pub i_interface: Option<String>,
    pub class: u8,
    pub subclass: u8,
    pub protocol: u8,
    pub alt_settings: Option<Vec<UsbAltSetting>>,
}

impl UsbInterface {
    pub fn _get_markup(&self) -> String {
        let mut interface_string = format!("Interface {}", self.b_interface_number);
        if let Some(name) = &self.i_interface {
            interface_string += format!(" (<b>{}</b>)", glib::markup_escape_text(name)).as_str();
        }
        interface_string += format!(
            " (class={}, subclass={}, protocol={})",
            self.class, self.subclass, self.protocol
        )
        .as_str();
        interface_string
    }
}

impl std::fmt::Display for UsbInterface {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let mut interface_string = format!("Interface {}", self.b_interface_number);
        if let Some(name) = &self.i_interface {
            interface_string += format!(" ({})", name).as_str();
        }
        interface_string += format!(
            " (class={}, subclass={}, protocol={})",
            self.class, self.subclass, self.protocol
        )
        .as_str();
        write!(f, "{}", interface_string)
    }
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbConfiguration {
    pub is_active: bool,
    pub b_configuration_number: Option<u8>,
    pub i_configuration: Option<String>,
    bm_attributes: Option<u8>,
    pub max_power_ma: Option<u16>,
    pub interfaces: Vec<UsbInterface>,
}

impl std::fmt::Display for UsbConfiguration {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let configuration_string = if let Some(number) = self.b_configuration_number {
            let mut string = format!("Configuration {}", number);
            if let Some(name) = &self.i_configuration {
                string += format!(" ({})", name).as_str();
            }
            if self.is_active {
                string += " (active)";
            }
            if let Some(power) = self.max_power_ma {
                string += format!(" ({} mA)", power).as_str();
            }
            string
        } else {
            "Active configuration".to_string()
        };
        write!(f, "{}", configuration_string)
    }
}

#[derive(serde::Serialize, serde::Deserialize)]
#[allow(non_camel_case_types)]
pub enum UsbDeviceSpeed {
    LOW,
    FULL,
    HIGH,
    SUPER,
    SUPER_PLUS,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbDevice {
    node_type: UsbDeviceTreeNodeType,
    raw_descriptor: Option<String>,

    // General attributes
    class: u8,
    subclass: u8,
    protocol: u8,

    pub vendor_id: String,
    pub product_id: String,
    pub serial_number: Option<String>,
    bcd_dev_version: String,
    pub bcd_usb_version: String,

    pub vendor_name: Option<String>,
    pub product_name: Option<String>,
    pub speed_mbps: Option<f64>,
    pub speed_type: Option<UsbDeviceSpeed>,

    bus_string: String,
    port_chain: Vec<u8>,

    // Nested structures
    pub can_open: bool,
    pub configurations: Vec<UsbConfiguration>,

    // Platform-dependant attributes
    linux_path: Option<String>,
    linux_bus: Option<u8>,
    /* windows_port: Option<u32>, // TODO
    macos_registry: Option<u64>,
    macos_location: Option<u32>, */
}

impl UsbDevice {
    pub fn _get_markup(&self) -> String {
        let speed_info = match &self.speed_type {
            None => "",
            Some(speed) => match speed {
                UsbDeviceSpeed::LOW => " (1.5 Mb/s)",
                UsbDeviceSpeed::FULL => " (12 Mb/s)",
                UsbDeviceSpeed::HIGH => " (480 Mb/s)",
                UsbDeviceSpeed::SUPER => " (5 Gb/s)",
                UsbDeviceSpeed::SUPER_PLUS => " (10 Gb/s)",
            },
        };
        let can_open_string = match self.can_open {
            true => "",
            false => " (<span foreground=\"red\"><b>locked</b></span>)",
        };
        let usb_version = &self.bcd_usb_version[1..2];
        let mut usb_subversion = self.bcd_usb_version[2..].replace("0", "");
        if usb_subversion.is_empty() {
            usb_subversion = "0".to_string();
        }
        let usb_version_info = format!(" (USB {}.{})", usb_version, usb_subversion);
        let device_string = format!(
            "Device <b>{}</b>:<b>{}</b> - <b>{} {}</b>{}{}{}",
            self.vendor_id.to_uppercase(),
            self.product_id.to_uppercase(),
            glib::markup_escape_text(&self.vendor_name.clone().unwrap_or("".to_string()))
                .to_string(),
            glib::markup_escape_text(&self.product_name.clone().unwrap_or("".to_string()))
                .to_string(),
            can_open_string,
            usb_version_info,
            speed_info
        );
        device_string
    }
}

impl std::fmt::Display for UsbDevice {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let speed_info = match &self.speed_type {
            None => "",
            Some(speed) => match speed {
                UsbDeviceSpeed::LOW => " (1.5 Mb/s)",
                UsbDeviceSpeed::FULL => " (12 Mb/s)",
                UsbDeviceSpeed::HIGH => " (480 Mb/s)",
                UsbDeviceSpeed::SUPER => " (5 Gb/s)",
                UsbDeviceSpeed::SUPER_PLUS => " (10 Gb/s)",
            },
        };
        let can_open_string = match self.can_open {
            true => "",
            false => " (locked)",
        };
        let usb_version = &self.bcd_usb_version[1..2];
        let mut usb_subversion = self.bcd_usb_version[2..].replace("0", "");
        if usb_subversion.is_empty() {
            usb_subversion = "0".to_string();
        }
        let usb_version_info = format!(" (USB {}.{})", usb_version, usb_subversion);
        let device_string = format!(
            "Device {}:{} - {} {}{}{}{}",
            self.vendor_id.to_uppercase(),
            self.product_id.to_uppercase(),
            self.vendor_name.clone().unwrap_or("".to_string()),
            self.product_name.clone().unwrap_or("".to_string()),
            can_open_string,
            usb_version_info,
            // self.serial_number.unwrap_or("".to_string()),
            speed_info
        );
        write!(f, "{}", device_string)
    }
}

#[derive(serde::Serialize, serde::Deserialize)]
pub enum UsbControllerType {
    XHCI,
    EHCI,
    OHCI,
    UHCI,
    VHCI,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbBus {
    node_type: UsbDeviceTreeNodeType,

    pub bus_string: String,
    driver_string: Option<String>,
    controller_type: Option<UsbControllerType>,

    pub readable_name: Option<String>,
    pub devices: Vec<UsbDevice>,

    // Platform-dependant attributes
    linux_path: Option<String>,
    linux_bus: Option<u8>,
    // TODO: Add macOS and Windows-related features (w/ cross compile or SSH disk ?)
}

impl std::fmt::Display for UsbBus {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        let bus_string = match &self.readable_name {
            Some(name) => format!("Bus {} - {}", self.bus_string, name),
            None => format!("Bus {}", self.bus_string),
        };
        write!(f, "{}", bus_string)
    }
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbDeviceTree(pub Vec<UsbBus>);

#[derive(serde::Serialize, serde::Deserialize)]
pub enum EndpointRespStatusCode {
    OK,
    NOK,
}

#[derive(serde::Serialize, serde::Deserialize)]
#[allow(non_camel_case_types)]
pub enum UsbDevicesEndpointRespErrorCode {
    LIST_DEVICES_NOK,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct UsbDevicesEndpointResp {
    status: EndpointRespStatusCode,
    error_code: Option<UsbDevicesEndpointRespErrorCode>,
    error_string: Option<String>,
    pub device_tree: Option<UsbDeviceTree>,
}

pub async fn get_usb_metadata() -> UsbDevicesEndpointResp {
    let mut device_tree = UsbDeviceTree(vec![]);

    let mut bus_id_to_devices: HashMap<String, Vec<UsbDevice>> = HashMap::new();

    let raw_devices = match nusb::list_devices().await {
        Ok(iter) => iter,
        Err(error) => {
            return UsbDevicesEndpointResp {
                status: EndpointRespStatusCode::NOK,
                error_code: Some(UsbDevicesEndpointRespErrorCode::LIST_DEVICES_NOK),
                error_string: Some(format!("Couldn't get devices: {:#?}", error)),
                device_tree: None,
            };
        }
    };

    // WIP Parse the devices information
    // Cf. file:///home/marin/nusb/target/doc/nusb/fn.list_devices.html

    for device in raw_devices {
        let linux_path;
        let linux_bus;

        #[cfg(target_os = "linux")]
        {
            linux_bus = Some(device.busnum());
            linux_path = Some(device.sysfs_path().display().to_string());
        }
        #[cfg(not(target_os = "linux"))]
        {
            linux_bus = None;
            linux_path = None;
        }

        let bus_string = device.bus_id().to_string();

        let mut configurations: Vec<UsbConfiguration> = vec![];

        let mut raw_descriptor: Option<String> = None;

        let can_open = match device.open().await {
            Ok(open_device) => {
                let descriptor = open_device.device_descriptor();
                let mut hex_data = hex::encode(descriptor.as_bytes());

                let active_config_number: Option<u8> = match open_device.active_configuration() {
                    Ok(active_config) => Some(active_config.configuration_value()),
                    Err(_) => None,
                };

                for config_desc in open_device.configurations() {
                    hex_data += &hex::encode(config_desc.as_bytes());
                    let mut interfaces: Vec<UsbInterface> = vec![];

                    for interface_desc in config_desc.interfaces() {
                        let mut alt_settings: Vec<UsbAltSetting> = vec![];

                        let first_alt_setting = interface_desc.first_alt_setting();

                        for alt_setting in interface_desc.alt_settings() {
                            let mut endpoints: Vec<UsbEndpoint> = vec![];

                            for endpoint in alt_setting.endpoints() {
                                endpoints.push(UsbEndpoint {
                                    b_endpoint_address: endpoint.address(),
                                    bm_attributes: endpoint.attributes(),
                                    direction: match endpoint.direction() {
                                        nusb::transfer::Direction::Out => UsbEndpointDirection::OUT,
                                        nusb::transfer::Direction::In => UsbEndpointDirection::IN,
                                    },
                                    transfer_type: match endpoint.transfer_type() {
                                        nusb::descriptors::TransferType::Control => {
                                            UsbEndpointTransferType::CONTROL
                                        }
                                        nusb::descriptors::TransferType::Isochronous => {
                                            UsbEndpointTransferType::ISOCHRONOUS
                                        }
                                        nusb::descriptors::TransferType::Bulk => {
                                            UsbEndpointTransferType::BULK
                                        }
                                        nusb::descriptors::TransferType::Interrupt => {
                                            UsbEndpointTransferType::INTERRUPT
                                        }
                                    },
                                    bytes_per_packet: endpoint.max_packet_size(),
                                    packets_per_microframe: endpoint.packets_per_microframe(),
                                    polls_between_microframe: endpoint.interval(),
                                })
                            }

                            alt_settings.push(UsbAltSetting {
                                b_alt_setting: alt_setting.alternate_setting(),
                                class: alt_setting.class(),
                                subclass: alt_setting.subclass(),
                                protocol: alt_setting.protocol(),
                                endpoints,
                            })
                        }

                        interfaces.push(UsbInterface {
                            b_interface_number: first_alt_setting.interface_number(),
                            i_interface: match first_alt_setting.string_index() {
                                Some(string_index) => open_device
                                    .get_string_descriptor(
                                        string_index,
                                        nusb::descriptors::language_id::US_ENGLISH,
                                        std::time::Duration::from_secs(1),
                                    )
                                    .await
                                    .ok(),
                                None => None,
                            },
                            class: first_alt_setting.class(),
                            subclass: first_alt_setting.subclass(),
                            protocol: first_alt_setting.protocol(),
                            alt_settings: Some(alt_settings),
                        })
                    }

                    configurations.push(UsbConfiguration {
                        is_active: active_config_number == Some(config_desc.configuration_value()),
                        b_configuration_number: Some(config_desc.configuration_value()),
                        i_configuration: match config_desc.string_index() {
                            Some(string_index) => open_device
                                .get_string_descriptor(
                                    string_index,
                                    nusb::descriptors::language_id::US_ENGLISH,
                                    std::time::Duration::from_secs(1),
                                )
                                .await
                                .ok(),
                            None => None,
                        },
                        bm_attributes: Some(config_desc.attributes()),
                        max_power_ma: Some((config_desc.max_power() as u16) * 2),
                        interfaces,
                    })
                }

                raw_descriptor = Some(hex_data);

                true
            }
            Err(_) => {
                let mut interfaces: Vec<UsbInterface> = vec![];

                for interface in device.interfaces() {
                    interfaces.push(UsbInterface {
                        b_interface_number: interface.interface_number(),
                        i_interface: interface.interface_string().map(str::to_string),
                        class: interface.class(),
                        subclass: interface.subclass(),
                        protocol: interface.protocol(),
                        alt_settings: None,
                    })
                }

                if interfaces.len() > 0 {
                    configurations.push(UsbConfiguration {
                        is_active: true,
                        b_configuration_number: None,
                        i_configuration: None,
                        bm_attributes: None,
                        max_power_ma: None,
                        interfaces: interfaces,
                    })
                }
                false
            }
        };

        if !bus_id_to_devices.contains_key(&bus_string) {
            bus_id_to_devices.insert(bus_string.clone(), vec![]);
        }
        bus_id_to_devices
            .get_mut(&bus_string)
            .unwrap()
            .push(UsbDevice {
                node_type: UsbDeviceTreeNodeType::DEVICE,
                raw_descriptor,

                class: device.class(),
                subclass: device.subclass(),
                protocol: device.protocol(),

                vendor_id: format!("{:04x}", device.vendor_id()),
                product_id: format!("{:04x}", device.product_id()),
                bcd_dev_version: format!("{:04x}", device.device_version()),
                bcd_usb_version: format!("{:04x}", device.usb_version()),

                vendor_name: device.manufacturer_string().map(str::to_string),
                product_name: device.product_string().map(str::to_string),
                serial_number: device.serial_number().map(str::to_string),
                speed_mbps: match device.speed() {
                    None => None,
                    Some(speed) => match speed {
                        nusb::Speed::Low => Some(1.5),
                        nusb::Speed::Full => Some(12.0),
                        nusb::Speed::High => Some(480.0),
                        nusb::Speed::Super => Some(5000.0),
                        nusb::Speed::SuperPlus => Some(10000.0),
                        _ => None,
                    },
                },
                speed_type: match device.speed() {
                    None => None,
                    Some(speed) => match speed {
                        nusb::Speed::Low => Some(UsbDeviceSpeed::LOW),
                        nusb::Speed::Full => Some(UsbDeviceSpeed::FULL),
                        nusb::Speed::High => Some(UsbDeviceSpeed::HIGH),
                        nusb::Speed::Super => Some(UsbDeviceSpeed::SUPER),
                        nusb::Speed::SuperPlus => Some(UsbDeviceSpeed::SUPER_PLUS),
                        _ => None,
                    },
                },

                bus_string,
                port_chain: device.port_chain().to_vec(),

                can_open,
                configurations,

                linux_path,
                linux_bus,
            });
    }

    for devices in bus_id_to_devices.values_mut() {
        // A. SORT DEVICES BY PORT CHAIN

        devices.sort_by_key(|item| item.port_chain.clone());

        /* B. ITERATE BACKWARDS OVER DEVICES AND NEST DESCENDING PORT CHAINS
        if device.port_chain.len() > 1 {
            let parent_key = (
                device.bus_string.clone(),
                device.port_chain[..device.port_chain.len() - 1].to_vec()
            );
            if let Some(parent) = bus_and_port_chain_to_device.get_mut(&parent_key) {
                parent.children.push(&device);
                bus_id_to_devices.get_mut(&device.bus_string).unwrap().retain(|x| **x != device);
            }
        } */
    }

    // Get buses information

    match nusb::list_buses().await {
        Ok(iter) => {
            let mut buses: Vec<nusb::BusInfo> = iter.collect();
            buses.sort_by_key(|item| item.bus_id().to_string());
            for bus in buses {
                let linux_bus;
                let linux_path;
                #[cfg(target_os = "linux")]
                {
                    linux_bus = Some(bus.busnum());
                    linux_path = Some(bus.sysfs_path().display().to_string());
                }
                #[cfg(not(target_os = "linux"))]
                {
                    linux_bus = None;
                    linux_path = None;
                }

                // Cf. file:///home/marin/nusb/target/doc/nusb/fn.list_buses.html

                device_tree.0.push(UsbBus {
                    node_type: UsbDeviceTreeNodeType::BUS,
                    devices: bus_id_to_devices
                        .remove(&bus.bus_id().to_string())
                        .unwrap_or(vec![]),

                    bus_string: bus.bus_id().to_string(),
                    driver_string: bus.driver().map(str::to_string),
                    controller_type: match bus.controller_type() {
                        // The original nusb::UsbControllerType type is not Serde serializable
                        None => None,
                        Some(value) => match value {
                            nusb::UsbControllerType::XHCI => Some(UsbControllerType::XHCI),
                            nusb::UsbControllerType::EHCI => Some(UsbControllerType::EHCI),
                            nusb::UsbControllerType::OHCI => Some(UsbControllerType::OHCI),
                            nusb::UsbControllerType::UHCI => Some(UsbControllerType::UHCI),
                            nusb::UsbControllerType::VHCI => Some(UsbControllerType::VHCI),
                            _ => None,
                        },
                    },

                    readable_name: bus.system_name().map(str::to_string),

                    linux_bus,
                    linux_path,
                });
            }
        }
        Err(_) => {
            // debug!("Couldn't get buses: {:#?}", error);

            // Fallback filling up the device tree with UsbDevices

            let mut bus_id_to_devices: Vec<(String, Vec<UsbDevice>)> =
                bus_id_to_devices.into_iter().collect();
            bus_id_to_devices.sort_by_key(|item| item.0.clone());

            for (bus_id, devices) in bus_id_to_devices {
                device_tree.0.push(UsbBus {
                    node_type: UsbDeviceTreeNodeType::BUS,
                    devices: devices,

                    bus_string: bus_id,
                    driver_string: None,
                    controller_type: None,

                    readable_name: None,

                    linux_bus: None,
                    linux_path: None,
                });
            }
        }
    };

    return UsbDevicesEndpointResp {
        status: EndpointRespStatusCode::OK,
        error_code: None,
        error_string: None,
        device_tree: Some(device_tree),
    };
}
