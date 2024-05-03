 # TinyTuya Example
# -*- coding: utf-8 -*-
"""
 TinyTuya - Smart Bulb RGB Music Test

 TODO: Figure out what strings to send to the bulb to
       represent real music data, beats, note, fades, etc.

 Author: Jason A. Cox
 For more information see https://github.com/jasonacox/tinytuya

"""
import tinytuya
import time
import json
import random

#tinytuya.set_debug()

print("TinyTuya - Smart Bulb Music Test [%s]\n" % tinytuya.__version__)
#print('TESTING: Device %s at %s with key %s version %s' %
#      (DEVICEID, DEVICEIP, DEVICEKEY, DEVICEVERS))


class FakeLamp():
    def status(self):
        return {"1": "on"}

    def set_mode(self, mode):
        print("Setting mode to %s" % mode)

    def set_colour(self, color):
        print("Setting color to %s" % color)


def create_lamp():
    with open("devices.json", encoding="utf-8") as f:
        data = json.load(f)

    #lamp = data["result"][0]
    lamp = data[0]
    # Connect to Tuya BulbDevice
    print("Creating")
    d = tinytuya.BulbDevice(lamp["id"], lamp["ip"], lamp["key"])
    d.set_version(float("3.3")) # IMPORTANT to always set version
    # Keep socket connection open between commands
    d.set_socketPersistent(True)
    return d


d = create_lamp()
# Show status of device
data = d.status()
print('\nCurrent Status of Bulb: %r' % data)

# Music Test
print('Setting to Music')
d.set_mode('music')
data = d.status()

# Send example music data to bulb
#  TODO: Figure out what the value does and how to use it to
#        represent real music data, beats, colors, fades
x = 0
def randomb():
    return random.randint(0, 255)

while True:
    value = "%02d01" % x
    print (" > Sending %s" % value)
    #payload = d.generate_payload(tinytuya.CONTROL, {"27": value})
    #payload = d.generate_payload(tinytuya.CONTROL, {"24": {"h":  random.randint(0, 360), "s": 50, "v": 100}})
    #d.send(payload)

    d.set_colour(randomb(), randomb(), randomb())

    time.sleep(random.randint(3, 6))

# Done
print('\nDone')
d.set_white()
