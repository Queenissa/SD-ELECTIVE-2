"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library

from adafruit_circuitplayground import cp
from time import sleep



cp.pixels.brightness = 1

index = 9

while True:
    if (index > 9):
        index = 0

    elif (index < 0):
        index = 9


    if (cp.switch == False):
        cp.pixels[index] = (255, 255, 255)
        sleep(0.5)
        cp.pixels[index] = (0, 0, 0)
        index-=1
        

    else:
        cp.pixels[index] = (255, 255, 255)
        sleep(0.5)
        cp.pixels[index] = (0, 0, 0)
        index+=1
   


      