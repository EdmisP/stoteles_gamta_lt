import logging
import json
import aiohttp
import async_timeout
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

CONF_STATION_ID = "station_id"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_STATION_ID): cv.string,
        vol.Optional(CONF_NAME, default="Air Quality Sensor"): cv.string,
    }
)

_LOGGER = logging.getLogger(__name__)

BASE_URL = "http://stoteles.gamta.lt/ap3"
API_URL = f"{BASE_URL}/SS/index.php"

POLLUTANTS = ["SO2", "NO2", "O3", "PM10", "PM25", "CO"]

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    station_id = config[CONF_STATION_ID]
    name = config[CONF_NAME]
    
    sensors = [LtuAirQualitySensor(name, station_id, pollutant) for pollutant in POLLUTANTS]
    async_add_entities(sensors, True)

class LtuAirQualitySensor(Entity):
    def __init__(self, name, station_id, pollutant):
        self._station_id = station_id
        self._pollutant = pollutant
        self._name = f"ltu_air_quality_{self._station_id}_{self._pollutant.lower()}"
        self._state = None
        self._unit = "ug/m3" if pollutant not in ["CO"] else "mg/m3"
    
    @property
    def name(self):
        return self._name
    
    @property
    def state(self):
        return self._state
    
    @property
    def unit_of_measurement(self):
        return self._unit
    
    async def async_update(self):
        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    # Pirma kreiptis į bazinį URL
                    async with session.get(BASE_URL) as _:
                        pass
                    
                    # Po to vykdyti užklausą į API
                    async with session.post(API_URL, 
                                           headers={'Content-Type': 'application/x-www-form-urlencoded'}, 
                                           data={"action": "updatemap"}) as response:
                        
                        if response.status != 200:
                            _LOGGER.error(f"API returned status code {response.status}")
                            return
                        
                        text = await response.text()
                        try:
                            data = json.loads(text)
                        except json.JSONDecodeError:
                            _LOGGER.error(f"Failed to parse JSON, response: {text}")
                            return
                        
                        if data.get("error") == "ok":
                            station_data = data["result"].get(self._station_id, {})
                            if station_data:
                                for channel in station_data.get("kanalai", []):
                                    if channel["kanalas"] == self._pollutant and channel["koncentracija"] is not None:
                                        self._state = channel["koncentracija"]
                                        return
                                self._state = None  # Jei nėra duomenų, palikti None
                            else:
                                _LOGGER.warning(f"No data found for station {self._station_id}")
                        else:
                            _LOGGER.error("Failed to fetch data from API")
        except Exception as e:
            _LOGGER.error(f"Error updating sensor: {e}")
