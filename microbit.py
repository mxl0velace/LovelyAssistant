# Imports go at the top
from microbit import *


heart = Image.HEART
diamond = Image('00700:'
                '07970:'
                '79997:'
                '07970:'
                '00700')
space = Image('00900:'
                '09990:'
                '99999:'
                '90909:'
                '06960')
club = Image('06960:'
                '60906:'
                '99999:'
                '60906:'
                '00900')

def angle_to_value(angle):
    if angle > 353:
        return "A"
    if angle < 20:
        return "A"
    if angle > 353 - 27:
        return "K"
    if angle > 353 - (27 * 2):
        return "Q"
    if angle > 353 - (27 * 3):
        return "J"
    return round((angle - 20) / 27) + 1

# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    initial = compass.heading()
    rolling = compass.heading()
    prev = -100
    while round(rolling/5) != round(prev/5):
        sleep(500)
        prev = rolling
        rolling = compass.heading()
    diff = rolling - initial
    if diff < 0:
        diff += 360
    
    value = angle_to_value(diff)
    display.show(value)
    sleep(500)
    display.clear()
    sleep(500)
    
    

# Code in a 'while True:' loop repeats forever
while True:
    display.show(club)
    sleep(1000)
    display.show("2")
    sleep(1000)
