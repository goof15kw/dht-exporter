#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import signal
import sys
import argparse
import random
import time
import Adafruit_DHT
from prometheus_client import start_http_server, Gauge

 
def signal_term_handler(signal, frame):
    print("got SIGTERM")
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)

# Create a metric to track time spent and requests made.
g_temperature = Gauge('dht_temperature', 'Temperature in celsius provided by dht sensor or similar', ['location'])
g_humidity = Gauge('dht_humidity', 'Humidity in percents provided by dht sensor or similar', ['location'])

def update_sensor_data(gpio_pin, location, sensor):
    """Get sensor data and sleep."""
    # get sensor data from gpio pin provided in the argument
    if sensor == "DHT11":
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, gpio_pin)
    elif sensor == "DHT22":
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, gpio_pin)
    elif sensor == "AM2302":
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, gpio_pin)
    else:
        print("Sensor {sensor} is unsupported. Supported sensors are: DHT11|DHT22|AM2302")
        exit(1)

    if humidity is not None and temperature is not None:
        if abs(temperature) < 100:     #If sensor returns veird value ignore it and wait for the next one
            g_temperature.labels(location).set('{0:0.1f}'.format(temperature))
        if abs(humidity) < 100:        #If sensor returns veird value ignore it and wait for the next one
           g_humidity.labels(location).set('{0:0.1f}'.format(humidity))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pull_time", type=int, default=60, help="Pull sensor data every X seconds.")
    parser.add_argument("-g", "--gpio",      type=int, nargs='+', help="Set GPIO pin id to listen for DHT sensor data.", required=True)
    parser.add_argument("-l", "--location",      type=str, nargs='+', help="Set location name.", required=True)
    parser.add_argument("-s", "--sensor",    type=str, nargs='+', help="Sensor model [DHT11|DHT22|AM2302].", default="DHT11")
    cli_arguments = parser.parse_args()

    if len(cli_arguments.gpio) != len(cli_arguments.location):
        print("The number of gpio pins set needs to be the same as number of locations set" \
              "\n Number of gpio pins: {g}\n Number of locations: {r}".format(g=len(cli_arguments.gpio), r=len(cli_arguments.location)))
        exit(1)
    # Start up the server to expose the metrics.
    start_http_server(8001)

    # Update temperature and humidity
    while True:
        for id, gpio_pin in enumerate(cli_arguments.gpio):
            update_sensor_data(gpio_pin, cli_arguments.location[id], cli_arguments.sensor[id])
        time.sleep(cli_arguments.pull_time)




