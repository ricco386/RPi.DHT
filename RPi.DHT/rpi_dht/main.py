#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE files,
# which you should have received as part of this distribution.
import sys
import argparse
from dht import Dht


def main():

    ap = argparse.ArgumentParser(prog='rpi-dht', description='''Python implementation for Adafruit_DHT sensor for
    Raspberry Pi. Script loads configuration from sensor.cfg that has to be created and run in infinte loop. For more
    info visit: https://github.com/ricco386/RPi.DHT''')
    ap.add_argument('--display', action='store_true', help='Display sensor reading described output.')
    ap.add_argument('--temperature', action='store_true', help='Display temperature in *C.')
    ap.add_argument('--humidity', action='store_true', help='Display humidity in percent.')
    args = ap.parse_args()

    sensor = Dht(args)

    if hasattr(args, 'display') and args.display:
        print(sensor.output())
    elif hasattr(args, 'temperature') and args.temperature:
        print(sensor.output(temp=True, desc=False))
    elif hasattr(args, 'humidity') and args.humidity:
        print(sensor.output(hum=True, desc=False))
    else:
        sensor.sense()

    sys.exit(0)


if __name__ == "__main__":
    # execute only if run as a script
    main()
