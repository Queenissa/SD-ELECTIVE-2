from microbit import *


while True:
    display1 = Image('90000:09000:00900:00090:00009')
    display2 = Image('09000:00900:00090:00009:90000')
    display3 = Image('00900:00090:00009:90000:09000')
    display4 = Image('00090:00009:90000:09000:00900')
    display5 = Image('00009:90000:09000:00900:00090')
    displayAll = [display1, display2,display3,display4,display5]
    display.show(displayAll, delay=700)