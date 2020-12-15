# Activty 5: Light Sensor Controlled LED's
from microbit import *
from time import *


brightness= 0
brightness_control= 0
position = 0
position_X = 0
position_Y = 0

while True:    
    brightness_control = (display.read_light_level() // 10) * 10 
    brightness = display.read_light_level() - brightness_control 
    position = display.read_light_level() // 50
    position_Y = 4 - position
    position_X = (display.read_light_level()-(position*50))// 10


    for i in range(5):
        if(i > position_Y):
            for j in range(5):
                display.set_pixel(j,i,9)

        if(i < position_Y):
            for j in range(5):
                display.set_pixel(j,i,0)
                
        if i == position_Y:
            for j in range(5):
                if(j < position_X):
                    display.set_pixel(j,i,9)

                if(j > position_X):
                    display.set_pixel(j,i,0)
               

    if (position_Y < 0):
        display.set_pixel(4,0, 9)
    else:
        display.set_pixel(position_X, position_Y, brightness)