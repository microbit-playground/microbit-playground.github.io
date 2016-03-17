"""
     Spin the Bottle
"""

from microbit import *
import random

# create a list with two items
message = [
    "Truth",
    "Dare",
]

# repeat forever
while True:
    display.show(Image.HAPPY)
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.scroll(random.choice(message))
