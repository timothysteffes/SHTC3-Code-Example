#!/usr/bin/env python
# encoding: utf-8

import adafruit_shtc3
import board
import json
import sys
import time
from functions import getPublicIP

#net = "eth0"
net = "wlan0"
expected_ip = "192.168.1.16"

# waiting for the network at boot. I know there is a setting, but it wasn't working for me.
waiting = True
counter = 0
while waiting:
    public_ip = getPublicIP(net)
    
    sys.stdout.write("[" + str(counter) + "] Waiting for IP Address " + expected_ip + ". Getting: " + public_ip + "\r")
    sys.stdout.flush()

    if expected_ip == public_ip:
        waiting = False
    else:
        counter = counter + 1
        
        if counter == 1000:
            waiting = False 
    
    time.sleep(1)

i2c = board.I2C()   # uses board.SCL and board.SDA
sht = adafruit_shtc3.SHTC3(i2c)

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    celsius, relative_humidity = sht.measurements
    fahrenheit = (celsius * 1.8) + 32
    return json.dumps({'temperature': "%0.1f F" % fahrenheit,
                       'humidity': "%0.1f %%" % relative_humidity})

if __name__ == '__main__':
    app.run(public_ip, 5000)