# ferien-api.de Binary sensor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![HACS: TBD](https://img.shields.io/badge/HACS-TBD-yellow.svg)](https://github.com/hacs/integration/blob/master/README.md)

> Home assistant binary sensor component to indicate if today is a german vacational day or not

## Installation

**Manual**

1. Copy the `ferienapidotde` folder into your `custom_components` folder that is located under the root of your `home assistant config`. If it does not exists you can create it (which probably means you never used a custom component before).
2. Throw down a minimal configuration

```yaml
binary_sensor:
  - platform: ferienapidotde
    state_code: HH  # State Hamburg
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
```

A list of all valid abbreviations for the german federal states can be found here: [https://www.datenportal.bmbf.de/portal/de/G122.html](https://www.datenportal.bmbf.de/portal/de/G122.html)

If you wantt to monitor multiple states you have to setup multiple sensors:

```yaml
binary_sensor:
  - platform: ferienapidotde
    name: Vacation (HH)
    state_code: HH
  - platform: ferienapidotde
    name: Vacation (SH)
    state_code: SH
```
