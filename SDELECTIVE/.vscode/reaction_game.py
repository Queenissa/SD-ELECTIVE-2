from adafruit_clue import clue
from random import randint
import time
import random

clue_display = clue.simple_text_display(title="REACTION GAME", title_color=clue.YELLOW, title_scale=1, text_scale = 2)


score_A = 0
score_B = 0
timer = 3




def displayRandomNumAndScore(randomNum,score_A,score_B):
    clue_display[2].text = str(randomNum).center(20)
    clue_display[2].color = clue.SKY

    clue_display[4].text = "Player A Score: " + str(score_A)
    clue_display[4].color = clue.GREEN

    clue_display[5].text = "Player B Score: " + str(score_B)
    clue_display[5].color = clue.CYAN


def playerScore(score):
    if randomNum % 2 == 0:
        score+=1
    else: 
        if(score < 1):
            score = 0
        else:
            score -= 1
    return score


# Display instructions
for i in range(timer, 0, -1):
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


    clue_display.show()

    clue_display[6].text = "Starts in " + str(i)
    clue_display[6].color = clue.RED
    time.sleep(1)
    if i==1:
        while True:

            randomNum = random.randint(0,100)

            clue_display[6].text = ""
            clue_display[3].text = ""
            clue_display[2].text = ""
            clue_display[1].text = ""
            clue_display[0].text = ""
        

            #Display winner
            if score_A>4:
                randomNum = "Player A wins"
            if score_B>4:
                randomNum = "Player B wins"
            
            displayRandomNumAndScore(randomNum,score_A,score_B)

            
            timeCtr = 1
            first = time.time()
            second = time.time()


            while timeCtr > 0:
                if(second - first >= 1):
                    timeCtr = 0
                else:
                    second = time.time()

                
                
                #Player A Score
                if clue.button_a:
                    score_A = playerScore(score_A)
                    break
        

                #Player B Score
                if clue.button_b:
                    score_B = playerScore(score_B)
                    break

            clue_display.show()

