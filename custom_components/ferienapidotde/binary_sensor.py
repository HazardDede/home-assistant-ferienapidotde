"""
Utilizes the api `ferien-api.de` to provide a binary sensor to indicate if
today is a german vacational day or not - based on your configured state.

For more details about this platform, please refer to the documentation at
https://github.com/HazardDede/home-assistant-ferienapidotde
"""

import logging
from datetime import datetime, timedelta

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.exceptions import PlatformNotReady
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

ALL_STATE_CODES = [
    "BW",
    "BY",
    "BE",
    "BB",
    "HB",
    "HH",
    "HE",
    "MV",
    "NI",
    "NW",
    "RP",
    "SL",
    "SN",
    "ST",
    "SH",
    "TH",
]

ATTR_START = "start"
ATTR_END = "end"
ATTR_NEXT_START = "next_start"
ATTR_NEXT_END = "next_end"
ATTR_VACATION_NAME = "vacation_name"
ATTR_DAYS_OFFSET = "days_offset"
ATTR_DAY_FOR_CHECK = "day_for_check"

CONF_NAME_DEFAULT = "Vacation Sensor"
CONF_STATE = "state_code"
CONF_DAYS_OFFSET = "days_offset"

ICON_OFF_DEFAULT = "mdi:calendar-remove"
ICON_ON_DEFAULT = "mdi:calendar-check"

# Don't rush the api. Every 12h should suffice.
MIN_TIME_BETWEEN_UPDATES = timedelta(hours=12)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_STATE): vol.In(ALL_STATE_CODES),
        vol.Optional(CONF_NAME, default=CONF_NAME_DEFAULT): cv.string,
        vol.Optional(CONF_DAYS_OFFSET, default=0): cv.positive_int
    }
)

SCAN_INTERVAL = timedelta(minutes=1)


async def async_setup_platform(
        hass, config, async_add_entities, discovery_info=None
):
    """Setups the ferienapidotde platform."""
    _, _ = hass, discovery_info  # Fake usage
    state_code = config.get(CONF_STATE)
    name = config.get(CONF_NAME)
    days_offset = config.get(CONF_DAYS_OFFSET)

    try:
        data_object = VacationData(state_code, days_offset)
        await data_object.async_update()
    except Exception as ex:
        import traceback

        _LOGGER.warning(traceback.format_exc())
        raise PlatformNotReady() from ex

    async_add_entities([VacationSensor(name, data_object)], True)


class VacationSensor(BinarySensorEntity):
    """Implementation of the vacation sensor."""

    def __init__(self, name, data_object):
        self._name = name
        self.data_object = data_object
        self._state = None
        self._state_attrs = {}

    @property
    def name(self):
        """Returns the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Return the icon for the frontend."""
        return ICON_ON_DEFAULT if self.is_on else ICON_OFF_DEFAULT

    @property
    def is_on(self):
        """Returns the state of the device."""
        return self._state

    @property
    def device_state_attributes(self):
        """Returns the state attributes of this device. This is deprecated but
        we keep it for backwards compatibility."""
        return self._state_attrs

    @property
    def extra_state_attributes(self):
        """Returns the state attributes of this device."""
        return self._state_attrs

    async def async_update(self):
        """Updates the state and state attributes."""
        import ferien

        await self.data_object.async_update()
        vacs = self.data_object.data
        days_offset = self.data_object.days_offset
        day_for_check = datetime.now() + timedelta(days=days_offset)
        cur = ferien.current_vacation(vacs=vacs,dt=day_for_check)
        if cur is None:
            self._state = False
            nextvac = ferien.next_vacation(vacs=vacs,dt=day_for_check)
            if nextvac is None:
                self._state_attrs = {}
            else:
                aligned_end = nextvac.end - timedelta(seconds=1)
                self._state_attrs = {
                    ATTR_NEXT_START: nextvac.start.strftime("%Y-%m-%d"),
                    ATTR_NEXT_END: aligned_end.strftime("%Y-%m-%d"),
                    ATTR_VACATION_NAME: nextvac.name,
                    ATTR_DAYS_OFFSET: days_offset,
                    ATTR_DAY_FOR_CHECK: day_for_check.strftime("%Y-%m-%d"),
                }
        else:
            self._state = True
            aligned_end = cur.end - timedelta(seconds=1)
            self._state_attrs = {
                ATTR_START: cur.start.strftime("%Y-%m-%d"),
                ATTR_END: aligned_end.strftime("%Y-%m-%d"),
                ATTR_VACATION_NAME: cur.name,
                ATTR_DAYS_OFFSET: days_offset,
                ATTR_DAY_FOR_CHECK: day_for_check.strftime("%Y-%m-%d"),
            }


class VacationData:  # pylint: disable=too-few-public-methods
    """Class for handling data retrieval."""

    def __init__(self, state_code, days_offset):
        """Initializer."""
        self.state_code = str(state_code)
        self.data = None
        self.days_offset = days_offset

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def async_update(self):
        """Updates the publicly available data container."""
        try:
            import ferien
            _LOGGER.debug(
                "Retrieving data from ferien-api.de for %s",
                self.state_code
            )
            self.data = await ferien.state_vacations_async(self.state_code)
        except Exception:  # pylint: disable=broad-except
            if self.data is None:
                raise
            _LOGGER.error(
                "Failed to update the vacation data. Re-using an old state"
            )
