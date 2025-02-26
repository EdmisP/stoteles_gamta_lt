# Home Assistant Lithuania Air Quality Integration

This is a custom integration for Home Assistant that retrieves air quality data from `stoteles.gamta.lt/ap3`.

## Features
- Fetches air quality data from Lithuanian monitoring stations.
- Supports multiple air pollutants: `SO2`, `NO2`, `O3`, `PM10`, `PM25`, `CO`.
- Creates separate sensors for each pollutant per station.

## Installation
1. **Download the files**
   Clone or download this repository and place the `ltu_air_quality` folder inside:
   ```
   config/custom_components/
   ```

2. **Ensure the correct file structure:**
   ```
   config/
   ├── custom_components/
   │   ├── ltu_air_quality/
   │   │   ├── sensor.py
   │   │   ├── manifest.json
   ```

3. **Restart Home Assistant**
   - Navigate to `Settings > System > Restart`

## Available Monitoring Stations
Here are the available monitoring stations and their respective `station_id`s:
```
0001: Vilnius, Senamiestis
0002: Vilnius, Lazdynai
0003: Vilnius, Žirmūnai
0004: Vilnius, Savanorių prosp.
0012: Panevėžys, Centras
0021: Naujoji Akmenė
0022: Šiauliai
0023: Mažeikiai
0031: Klaipėda, Centras
0033: Klaipėda, Šilutės pl.
0041: Kaunas, Dainava
0042: Jonava
0043: Kėdainiai
0044: Kaunas, Noreikiškės
0051: Aukštaitija
0052: Dzūkija
0053: Žemaitija
```

## Configuration
Add the following to your `configuration.yaml` file:
```yaml
sensor:
  - platform: ltu_air_quality
    station_id: "0033"

  - platform: ltu_air_quality
    station_id: "0031"
```

Each `station_id` represents a different air quality monitoring station.

## Viewing the Sensors
After restarting Home Assistant, the new sensors will be available in `Developer Tools > States`. Example sensor names:
```
sensor.ltu_air_quality_0033_co
sensor.ltu_air_quality_0033_no2
sensor.ltu_air_quality_0031_pm10
```

## Logs and Debugging
If the integration is not working as expected, check logs in:
- `Settings > System > Logs`
- Or enable debug logging by adding this to `configuration.yaml`:
  ```yaml
  logger:
    default: warning
    logs:
      custom_components.ltu_air_quality: debug
  ```

