import time
from adafruit_circuitplayground import cp
 
def scale_range(value):
    return value / 288 * 9
 
while True:
    peak = scale_range(cp.light)
    for i in range(10):
        if i <= peak:
            if peak < 1:
                color =  int(255*cp.light/32)
                cp.pixels[0] = (color, color, color)
            elif peak < 2 and peak >= 1:
                color =  int(255*(cp.light-32)/32)
                print(color)
                cp.pixels[1] = (color, color, color)
            elif peak < 3 and peak >= 2:
                 color = int(255*(cp.light-64)/32)
                 cp.pixels[2] = (color, color, color)
            elif peak < 4 and peak >= 3:
                 color = int(255*(cp.light-96)/32)
                 cp.pixels[3] = (color, color, color)
            elif peak < 5 and peak >= 4:
                 color = int(255*(cp.light-128)/32)
                 cp.pixels[4] = (color, color, color)
            elif peak < 6 and peak >= 5:
                 color = int(255*(cp.light-160)/32)
                 cp.pixels[5] = (color, color, color)
            elif peak < 7 and peak >= 6:
                 color = int(255*(cp.light-192)/32)
                 cp.pixels[6] = (color, color, color)
            elif peak < 8 and peak >= 7:
                 color = int(255*(cp.light-224)/32)
                 cp.pixels[7] = (color, color, color)
            elif peak < 9 and peak >= 8:
                 color = int(255*(cp.light-256)/32)
                 cp.pixels[8] = (color, color, color)
            elif peak < 10 and peak >= 2:
                 color = int(255*(cp.light-288)/32)
                 cp.pixels[9] = (color, color, color)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)
    
