from microbit import *
from time import sleep

index = 0

while True:
    if index > 28:
        index = 0
    dot = "00000:00000:00000:00000:00000"
    dot_list = list(dot)
    dot_length = len(dot_list)

    for i in range(0, dot_length):
        if dot_list[i] == ':':
            continue

        if i == index:
            dot_list[i] = '9'
        else:
            dot_list[i] = '0'
    
    index = index + 1
    dot = "".join(dot_list)
    display.show(Image(dot))
    sleep(0.5)



    
  

