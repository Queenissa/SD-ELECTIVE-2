import time
from adafruit_circuitplayground import cp

while True:
    # cp.red_led = True
    # time.sleep(0.5)
    # cp.red_led = False
    # time.sleep(o.5)


                                                        

    # print("Light:", cp.light)
    # print(cp.light)
    # time.sleep(0.1)


    # cp.pixels.auto_write = False
    # cp.pixels.brightness = 0.3
    
    
    # def scale_range(value):
    #     """Scale a value from 0-320 (light range) to 0-9 (NeoPixel range).
    #     Allows remapping light value to pixel position."""
    #     return round(value / 320 * 9)
    
    
    # while True:
    #     peak = scale_range(cp.light)
    #     print(cp.light)
    #     print(int(peak))
    
    #     for i in range(10):
    #         if i <= peak:
    #             cp.pixels[i] = (0, 255, 255)
    #         else:
    #             cp.pixels[i] = (0, 0, 0)
    #     cp.pixels.show()
    #     time.sleep(0.05)

    # if cp.button_a:
    #     print("button a aprssed")
    #     cp.red_led = True
    # else:
    #     cp.red_led = False

    # cp.pixels.brightness = 0.3
    # cp.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!
 

    # if cp.button_a:
    #     cp.pixels[2] = (0, 255, 0)
    # else:
    #     cp.pixels[2] = (0, 0, 0)
 
    # if cp.button_b:
    #     cp.pixels[7] = (0, 0, 255)
    # else:
    color = int(255 * cp.light / 320)
    cp.pixels[0] = (color, color, color)
    cp.pixels[1] = (color, color, color)
    cp.pixels[2] = (color, color, color)
    cp.pixels[3] = (color, color, color)
    cp.pixels[4] = (color, color, color)
    cp.pixels[5] = (color, color, color)
    cp.pixels[6] = (color, color, color)
    cp.pixels[7] = (color, color, color)
    cp.pixels[8] = (color, color, color)
    cp.pixels[9] = (color, color, color)