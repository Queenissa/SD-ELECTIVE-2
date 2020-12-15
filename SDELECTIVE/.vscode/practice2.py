from microbit import *
from time import sleep


while True:
#     # display.scroll("Hello World!")
#     # display.show(Image.HAPPY)
#     # boat = Image("05050:"
#     #             "05050:"
#     #             "05050:"
#     #             "99999:"
#     #             "09990")

#     # display.show(boat)
#     # display.show(Image.ALL_ARROWS, loop=True, delay=1000)
#     # dot = Image("90000:00000:00000:00000:00000")
#     # display.show(dot)
#     # sleep(1)

#     sleep(10000)
#     display.scroll(str(button_a.get_presses()))

# from adafruit_clue import clue

# while True:
#     clue.white_leds = True

    light = display.read_light_level()
    print("{}".format(light))
    sleep(0.2)
