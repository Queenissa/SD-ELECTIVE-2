from adafruit_circuitplayground import cp
from time import sleep


i=9
# ctr=0


while True:
    if i > 9:
        i=0
    elif i < 0:
        i=9

    cp.pixels[i] = (255,255,255)
    sleep(1)
    cp.pixels[i] = (0,0,0)
    i-=1

   