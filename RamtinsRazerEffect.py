# TODO: Media Buttons

from threading import Thread
import time
import numpy as np
from getConfig import *
from key import Key

from pynput.keyboard import  Listener
from openrazer.client import DeviceManager

device_manager = DeviceManager()
device = device_manager.devices[0]
if not device.fx.advanced:
    print("ERROR: Device not supported")
    quit()

# Disable daemon effect syncing.
# Without this, the daemon will try to set the lighting effect to every device.
device_manager.sync_effects = False

#Custom key thread classes
keys = []


def getKeyMapping(key):
    try:
        if hasattr(key, 'vk') and not key.vk:
            return KEY_MAPPING[F"Numpad-{key.char}"]
        else:
            return KEY_MAPPING[str(key).lower()]
    except:
        print(F"Error key {key} not found returning (0,1)")
        return (0,1)

def reactivePress(key):
    xy = getKeyMapping(key)
    keys[xy[0]][xy[1]].setReact()
    update()

def reactiveRelease(key):
    xy = getKeyMapping(key)
    keys[xy[0]][xy[1]].setAnimation() 

def init():
    # Set static colors for each zone
    rows, cols = device.fx.advanced.rows, device.fx.advanced.cols

    for row in range(rows):
        rows = []
        for col in range(cols):
            key = Key(row,col,device.fx.advanced.matrix,update)
            rows.append(key)
        keys.append(rows)

def update():
    device.fx.advanced.draw()

if __name__ == "__main__":
    init()
    update()

    # Collect events until released
    with Listener(
            on_press=reactivePress,
            on_release=reactiveRelease) as listener:
        listener.join()