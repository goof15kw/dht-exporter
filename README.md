# DHT Exporter for Raspberry PI with docker

> Note: This project has been forked from matejp/dht-exporter.
> Note: This project has been forked from Koma-Andrea/dht-exporter
I've rewritten part of the code to be compatible with docker images and make user of environment variables.

## Usage:

```bash
git clone https://github.com/Koma-Andrea/dht-exporter
cd dht-exporter
docker build -t dht-exporter .
docker run --privileged dht-exporter
```

## You can override variables to fit you needs:

```bash
# Export those values:
# SENSOR Supported Adafruit_DHT sensors:DHT11|DHT22|AM2302
docker run --privileged -e SENSOR=DHT22 dht-exporter
# PULL: pull interval
docker run --privileged -e PULL=20 dht-exporter
# GPIO: GPIO PIN (note the phisical pin number is not the GPIO number IE phisical pin 7 is GPIO 4 https://pinout.xyz)
docker run --privileged -e GPIO=4 dht-exporter
# ROOM: The physical room in which the RPi is running (is arbitrary)
docker run --privileged -e ROOM=torture\ room dht-exporter
```

## If you want you can integrate the build in docker-compose:
```yaml
---
version: '3.2'
services:
  dht_exporter:
    build:
      context: https://github.com/Koma-Andrea/dht-exporter.git
    container_name: "dht"
    privileged: true
    restart: "always"
    ports:
      - 8001:8001
```

Feel free to contribute.
