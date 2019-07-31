# Dht Exporter

> Note: This project has been forked from matejp/dht-exporter.

I've rewritten part of the code to be compatible with docker images and make user of environment variables.

Usage:

```bash
git clone https://github.com/Koma-Andrea/dht-exporter
cd dht-exporter
docker build -t dht-exporter .
docker run dht-exporter
```