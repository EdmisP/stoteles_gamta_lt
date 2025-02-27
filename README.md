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

## Home Assistant Gauge Meter Examples
You can visualize air quality values using the Home Assistant gauge meter. Below are some examples with severity levels based on the thresholds from `stoteles.gamta.lt/ap3`.

### PM10 (Particulate Matter 10)
```yaml
type: gauge
entity: sensor.ltu_air_quality_0031_pm10
name: KD10
needle: true
severity:
  green: 16
  yellow: 31
  red: 51
max: 100
min: 0
```

### PM2.5 (Particulate Matter 2.5)
```yaml
type: gauge
entity: sensor.ltu_air_quality_0033_pm25
name: KD2.5
needle: true
severity:
  green: 11
  yellow: 21
  red: 26
max: 75
```

### Carbon Monoxide (CO)
```yaml
type: gauge
entity: sensor.ltu_air_quality_0031_co
name: CO
severity:
  green: 3
  yellow: 7
  red: 11
needle: true
max: 13
```

### Nitrogen Dioxide (NO2)
```yaml
type: gauge
entity: sensor.ltu_air_quality_0031_no2
name: NO2
severity:
  green: 51
  yellow: 101
  red: 201
needle: true
max: 400
```

### Sulfur Dioxide (SO2)
```yaml
type: gauge
entity: sensor.ltu_air_quality_0031_so2
name: SO2
needle: true
severity:
  green: 51
  yellow: 101
  red: 301
max: 500
```

### Ozone (O3)
```yaml
type: gauge
entity: sensor.ltu_air_quality_0033_o3
name: O3
severity:
  green: 61
  yellow: 121
  red: 181
needle: true
max: 240
```

These gauge meters provide an easy way to track air quality levels directly in your Home Assistant dashboard.

