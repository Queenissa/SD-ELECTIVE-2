from adafruit_clue import clue
import random
from random import randint
import time

display = clue.simple_text_display(title="Reaction Game", title_color=(255,99,71), title_scale=2)

intro = "Introduction:"
playerA = "Player A presses A"
playerB = "Player B presses B"
instruction = "Press if the number is divisible by 2"
score = "Maximum score of 5"
start = "Starts in"
scoreA = 0
scoreB = 0


playerAscore = "Player A score: "
playerBscore = "Player B score: "

def scoreGame(score):
    if(randomNumber % 2 == 0):
        score = score + 1
    else: 
        if(score < 1):
            score = 0
        else:
            score -= 1
    return score


def showDisplay(randomNumber, scoreA,scoreB):
    display[6].text = str(randomNumber).center(20)
    display[6].color= clue.WHITE
    display[6].scale = 2

    display[13].text = playerAscore+ str(scoreA) 
    display[15].text = playerBscore+ str(scoreB)



    
number = 3
for i in range(number, 0, -1):
    display[2].text = intro
    display[2].color= clue.GREEN
    display[2].scale=2

    display[4].text = playerA
    display[4].color= clue.WHITE
    display[4].scale=2

    display[6].text = playerB
    display[6].color= clue.WHITE
    display[6].scale=2

    display[8].text = instruction
    display[8].color= clue.BLUE
    display[8].scale=2

    display[10].text = score
    display[10].color= clue.YELLOW
    display[10].scale=2

    display[12].color= clue.RED
    display[12].scale= 2

    display[13].color= clue.GOLD
    display[13].scale= 2

    display[15].color= clue.GOLD
    display[15].scale= 2
    display.show()
    display[12].text = start + " " + str(i)
    time.sleep(1)
    if(i == 1):
        while True:
            # print(randint(0,100)) 
            randomNumber = random.randint(0,100)

            display[2].color= clue.BLACK
            display[4].color = clue.BLACK
            display[6].color = clue.BLACK
            display[8].color = clue.BLACK
            display[10].color = clue.BLACK
            display[12].color = clue.BLACK

            ctr = 1
            mes1 = time.time()
            mes2 = time.time()

            if(scoreA > 4):
                randomNumber = "Player A wins"
            if(scoreB > 4):
                randomNumber = "Player B wins"

            showDisplay(randomNumber,scoreA,scoreB)

            while ctr > 0: #epoch
                if(mes2 - mes1 >= 1):
                    ctr = 0
                else:
                    mes2 = time.time()

                if(clue.button_a):
                    # print(f"button a is clicked! {randomNumber}")
                    scoreA = scoreGame(scoreA)
                    # score1+=1
                    # print(score1)
                    break
                if(clue.button_b):
                    # print(f"button b is clicked! {randomNumber}")
                    scoreB = scoreGame(scoreB)
                    # score2+=1
                    # print(score2)
                    break


