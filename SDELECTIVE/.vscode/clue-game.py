from adafruit_clue import clue
from time import sleep
import random
from random import randint
# from adafruit_slideshow import SlideShow, PlayBackDirection


score_A = 0
score_B = 0
ctr = 4


clue_display = clue.simple_text_display(title="REACTION GAME", title_color=clue.YELLOW, title_scale=1, text_scale = 2)

clue_display[0].text = "Instructions:"
clue_display[0].color = clue.GREEN

clue_display[1].text = "Player A presses A"
clue_display[1].color = clue.WHITE

clue_display[2].text = "Player B presses B"
clue_display[2].color = clue.WHITE

clue_display[3].text = "Press if the number"
clue_display[3].color = clue.SKY

clue_display[4].text = " is divisible by 2"
clue_display[4].color = clue.SKY

clue_display[5].text = "Maximum score of 5"
clue_display[5].color = clue.YELLOW


ctr-=1
clue_display[6].text = "Starts in " + str(ctr)
clue_display[6].color = clue.RED

clue_display.show()
if ctr==1:
    while True:
        clue_display[6].text = ""
        # clue_display[5].text = ""
        # clue_display[4].text = ""
        clue_display[3].text = ""
        clue_display[2].text = ""
        clue_display[1].text = ""
        clue_display[0].text = ""
    


        clue_display[4].text = "Player A Score: " + str(score_A)
        clue_display[4].color = clue.GREEN

        clue_display[5].text = "Player B Score: " + str(score_B)
        clue_display[5].color = clue.CYAN


        randomNum = random.randint(randint(1,100))
        clue_display[2].x = 100
        clue_display[2].text =  randomNum
        clue_display[2].color = clue.SKY
        sleep(1)


        #Player A Score
        if clue.button_a and randomNum % 2==0:
            score_A+=1
        else:
            if score_A <1:
                score_A = 0
            else:
                score_A-=1
            break
        

        #Player B Score
        if clue.button_b and randomNum % 2==0:
            score_B+=1
        else:
            if score_B<1:
                score_B = 0
            else:
                score_B-=1
            break


        #Display winner
        if score_A>4:
             clue_display[2].text = "Player A wins"
        if score_B>4:
             clue_display[2].text = "Player B wins"

         
        
        clue_display.show()
    
  
 

    

    
  


    






