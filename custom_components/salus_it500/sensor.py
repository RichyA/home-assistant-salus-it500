"""Sensor platform for salus_it500."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .const import DOMAIN
from .coordinator import SalusIt500DataUpdateCoordinator
from .entity import SalusIt500Entity

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="salus_it500",
        name="Integration Sensor",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        SalusIt500Sensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class SalusIt500Sensor(SalusIt500Entity, SensorEntity):
    """salus_it500 Sensor class."""

    def __init__(
        self,
        coordinator: SalusIt500DataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")
