#!/usr/bin/env python
import json
import requests
import serial
import time

url = "http://b.phodal.com/athome/1"
serialport = serial.Serial("/dev/ttyACM0", 9600)

while True:
    try:
        response = requests.get(url)
        status = response.json()[0]['led1']

        if status in (0, 1):
            serialport.write(str(status))

    except requests.exceptions.RequestException as e:
        print(f"Error in HTTP request: {e}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    except serial.SerialException as e:
        print(f"Error in serial communication: {e}")

    time.sleep(1)
