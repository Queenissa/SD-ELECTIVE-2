from adafruit_clue import clue
from time import sleep


ctr = 0
clue_display = clue.simple_text_display(text_scale=2)
clue_display[2].text = "This is a message. " 


while True:
    temp = clue_display[2].text[0]
    clue_display[2].text = clue_display[2].text[1:] + temp
    clue_display[2].text = clue_display[2].text if ctr % 2 else ""
    clue_display[2].color = clue.AQUA
    sleep(0.5)
    ctr+=1

    clue_display.show()


