# Presenting DiagNG: After QCSuper, a new open-source initiative for freeing up mobile baseband Diag protocols

You may have heard of our [QCSuper](https://github.com/P1sec/QCSuper) tool, originally [released in 2019](https://www.p1sec.com/blog/presenting-qcsuper-a-tool-for-capturing-your-2g-3g-4g-air-traffic-on-qualcomm-based-phones), which brought up a breakthrough of simplicity and ergonomy in the task of producing sample **2G/3G/4G/5G air interface captures** ("OTA RRC logs") to the **PCAP format**, usable in [Wireshark](https://www.wireshark.org/) thanks to the [GSMTAP](https://osmocom.org/projects/baseband/wiki/GSMTAP) convention.

Since QCSuper has been released, it had the opportunity to stockpile [30 references on Google Scholar](https://scholar.google.com/scholar?q=%22qcsuper%22) and [almost 1.7k stars](https://github.com/P1sec/QCSuper/stargazers) on Github, a rare feat for a niche telecom security pedagogy and research tool, and we're frequently hearing about customer and telco operators using it in real-world conditions for device testing.

Today, **we want to push the interoperability and protocol openness exercise further**. QCSuper was a CLI (command line interface)-based tool, which limited its usability and capacity to be extended without impacting the usability of its usage notice.

We are today proud to present **[DiagNG](https://github.com/P1sec/DiagNG), a new GUI-based software** that should **embody as the sequel for QCSuper**. DiagNG is right now [available for Linux users](https://github.com/P1sec/DiagNG#install) and already contains the [key features from QCSuper](https://github.com/P1sec/DiagNG#feature-list), with [more to come](https://github.com/P1sec/DiagNG#roadmap).

<p align="center">
<img src="https://github.com/P1sec/DiagNG/blob/main/packaging/screenshots/light/global-screen-focus.png?raw=true" alt="Application main screen + device screen + Wireshark"><br><em>Screenshot of the main features of DiagNG</em>
</p>

<pre>
flatpak install -y https://p1sec-foss.gitlab.io/flatpak/diagng.flatpakref
flatpak run com.p1security.diagng
</pre>
<p align="center"><em>Install and run DiagNG in two commands on Linux</em></p>

We hope that you will enjoy it as an early Christmas gift! 🙌

Currently DiagNG can produce PCAP/GSMTAP captures for Qualcomm Snapdragon basebands like QCSuper does, but we would love to support reading from other baseband vendors such as Qualcomm, Mediatek or HiSilicon in the future! We are also looking forward to implement more baseband Diag protocol features.

For now, the features of DiagNG largely overlap with these of QCSuper in addition to the nice GUI, but, as a video is ofter worth a thousand words, feel free to watch the below in order to see it in direct operation:

https://github.com/user-attachments/assets/665e3498-11e4-4e00-8968-ea8ea15bd000

## Also NR/5G compatible!

DiagNG also supports producing NR/5G RRC logs in Wireshark, using the soon-to-be-standardized [GSMTAP v3](https://gitea.osmocom.org/peremen/gsmtapv3/src/branch/master/GSMTAPv3.md) protocol encapsulation format, already produced by other tools like SCAT.

<p align="center">
<img src="https://github.com/P1sec/DiagNG/blob/refs/heads/main/packaging/screenshots/light/5g-wireshark-screenshot-detailed-nocursor.png?raw=true" width="600" alt="A 5G/NR RRC log opened in Wireshark"><br><em>Screenshot of a NR/5G RRC log produced by DiagNG, opened in Wireshark</em>
</p>

For this, it prompts the user to install a custom Lua Wireshark GSMTAP v3 plug-in, allowing to leverage the NR/5G decoding abilities of Wireshark without the need of waiting for the upstream to push a full implementation.

## Under the hood

DiagNG is an open-source tool released under the GPL v3 license, leveraging the GTK 4/Adwaita toolkit in order to provide a sleek UI and UX to the users, and [Flatpak-based packaging](https://github.com/P1sec/DiagNG#install-gui-on-linux-flatpak) for Linux-first integration.

[Ubuntu](https://github.com/P1sec/DiagNG/tree/main#install-guicli-on-ubuntu-ppa) and [Archlinux](https://github.com/P1sec/DiagNG/tree/main#install-guicli-on-archlinux-aur) packages are also available as a second distribution channel.

It also uses the GLib event loop for better parallelism, communicates with other system components such as ADB, ModemManager and UDev (see [screenshots](https://github.com/P1sec/DiagNG#readme)) for slick integration to the Linux desktop, and ultimately integrates the [**Kaitai Struct library**](https://kaitai.io/) for standarized, interoperable **[definitions of vendor baseband protocol diagnostic interfaces](https://github.com/P1sec/DiagNG/tree/main/struct)**.

## Want to know more about it?

Feel free to [**read the original presentation blog post for QCSuper**](https://www.p1sec.com/blog/presenting-qcsuper-a-tool-for-capturing-your-2g-3g-4g-air-traffic-on-qualcomm-based-phones) to know more about what DiagNG does under the hood.

Feel free to [**find the general information and install instructions**](https://github.com/P1sec/DiagNG#readme) for the tool on Github, and/or [chat with us on Matrix](https://matrix.to/#/#diagng:matrix.org) for getting in touch and perhaps helping us to improve this new open-source tool!
