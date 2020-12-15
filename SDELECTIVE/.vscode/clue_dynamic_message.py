from adafruit_clue import clue
from time import sleep

clue_display = clue.simple_text_display(text_scale = 2)

 
ctr = 0
clue_display[2].text = "This message moves from right to left... "
clue_display[4].text = "This message moves from left to right... "

while True:
    clue_display[0].text = "Message Streamer"
    clue_display[0].color = clue.RED
 

    clue_display[2].color = clue.YELLOW
    temp = clue_display[2].text[0]
    clue_display[2].text = clue_display[2].text[1:] + temp
 
    
    clue_display[4].color = clue.WHITE
    temp = clue_display[4].text[-1:]
    clue_display[4].text = temp + clue_display[4].text[: -1]
 

    clue_display[6].text = "This message blinks" if ctr % 2 == 0 else ""
    clue_display[6].color = clue.SKY
    ctr += 1
    sleep(0.2)

    clue_display.show()

 

   

  