"""
    Harry Potter Sorting Hat

    Copyright (c) 2016 Various Authors

    MIT  Licence

"""
# import microbit and random modules
from microbit import *
import random

# create a list of strings called HOUSES
HOUSES   = ["Gryffindor",
            "Slytherin",
            "Ravenclaw",
            "Hufflepuff",
           ]

# create an endless loop waiting for button_a to be pressed
while True:
    if button_a.is_pressed():
        display.scroll(random.choice(HOUSES))
    sleep(100)
