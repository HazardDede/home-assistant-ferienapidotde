[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]](hacs)
![Project Maintenance][maintenance-shield]

Home assistant binary sensor component to indicate if today is a german vacational day or not

{% if not installed %}
## Installation

1. Click install.
1. Add `ferienapidotde` to your `configuration.yaml`

```yaml
binary_sensor:
  - platform: ferienapidotde
    state_code: HH  # Federal state of Hamburg
```
{% endif %}

## Configuration

To integrate `ferienapidotde` to your Home Assistant instance, you need to add the following section to your `configuration.yaml`:

Minimal example:

```yaml
binary_sensor:
  - platform: ferienapidotde
    state_code: HH
```

Full example:

Not so much you can do here but for the sake of completness.

```yaml
  - platform: ferienapidotde
    name: Vacation (HH)
    state_code: HH
```

A list of all valid abbreviations for the german federal states can be found here: [https://www.datenportal.bmbf.de/portal/de/G122.html](https://www.datenportal.bmbf.de/portal/de/G122.html)

If you want to monitor multiple states you have to setup multiple sensors:

```yaml
binary_sensor:
  - platform: ferienapidotde
    name: Vacation (HH)
    state_code: HH
  - platform: ferienapidotde
    name: Vacation (SH)
    state_code: SH
```

<!---->

***

[commits-shield]: https://img.shields.io/github/commit-activity/y/HazardDede/home-assistant-ferienapidotde.svg?style=for-the-badge
[commits]: https://github.com/HazardDede/home-assistant-ferienapidotde/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/HazardDede/home-assistant-ferienapidotde.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Dennis%20Muth%20%40HazardDede-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/HazardDede/home-assistant-ferienapidotde.svg?style=for-the-badge
[releases]: https://github.com/HazardDede/home-assistant-ferienapidotde/releases