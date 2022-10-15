# ferien-api.de binary sensor

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]](hacs)
![Project Maintenance][maintenance-shield]

> Home assistant binary sensor component to indicate if today is a german vacational day or not

## Installation

**HACS**

1. Make sure the [HACS](https://github.com/custom-components/hacs) component is installed and working.
2. Add this github repository https://github.com/HazardDede/home-assistant-ferienapidotde as custom integration repository in HACS settings.
3. Install the integration `ferienapidotde` and update home assistant configuration accordingly. You need to restart home assistant for the changes to take effect.

**Manual**

1. Copy the `ferienapidotde` folder into your `custom_components` folder that is located under the root of your `home assistant config`. If it does not exists you can create it (which probably means you never used a custom component before).
2. Throw down a minimal configuration

```yaml
binary_sensor:
  - platform: ferienapidotde
    state_code: HH  # Federal state of Hamburg
```

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
    days_offset: 1  # Offset = 1 -> Is there any vacation tomorrow? Can be negative as well!
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
  - platform: ferienapidotde
    name: Vacation (HH) + 3 days
    days_offset: 3
    state_code: HH
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