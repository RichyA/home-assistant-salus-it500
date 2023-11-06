# Salus it500

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]

_Integration to integrate with [Salus it500 Wireless Internet Controlled Thermostat][salus_it500_product]._

Note: This project is mainly for personal use. It meets my requirements and I'm unlikely to invest too much time in broadening the scope.

**This integration will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from Salus it500 API.
`switch` | Switch something `True` or `False`.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `salus_it500`.
1. Download _all_ the files from the `custom_components/salus_it500/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Salus it500"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[salus_it500_product]: https://saluscontrols.com/gb/product/it500-wireless-internet-controlled-thermostat/
[commits-shield]: https://img.shields.io/github/commit-activity/y/RichyA/home-assistant-salus-it500?style=for-the-badge
[commits]: https://github.com/RichyA/home-assistant-salus-it500/commits/main
[license-shield]: https://img.shields.io/github/license/RichyA/home-assistant-salus-it500.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Richard%20Archer%20%40RichyA-blue?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/RichyA/home-assistant-salus-it500?style=for-the-badge
[releases]: https://github.com/RichyA/home-assistant-salus-it500/releases
