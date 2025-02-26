# Home Assistant Lithuania Air Quality Integration

This is a custom integration for Home Assistant that retrieves air quality data from `stoteles.gamta.lt/ap3`.

## Features
- Fetches air quality data from Lithuanian monitoring stations.
- Supports multiple air pollutants: `SO2`, `NO2`, `O3`, `PM10`, `PM25`, `CO`.
- Creates separate sensors for each pollutant per station.

## Installation
1. **Download the files**
   Clone or download this repository and place the `stoteles_gamta_lt` folder inside:
   ```
   config/custom_components/
   ```

2. **Ensure the correct file structure:**
   ```
   config/
   ├── custom_components/
   │   ├── ltu_air_quality/
   │   │   ├── __init__.py
   │   │   ├── sensor.py
   │   │   ├── manifest.json
   ```

3. **Restart Home Assistant**
   - Navigate to `Settings > System > Restart`

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

