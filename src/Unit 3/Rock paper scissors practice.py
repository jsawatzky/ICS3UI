#PLAYS ROCK PAPER SCISSORS ONLY ONCE, BUT MAKES SURE THE USER
#ENTERS A VALID CHOICE

from random import *

compScore = 0
humScore = 0

while compScore < 3 and humScore < 3:
    questionWording = "What move would you like to pick (rock, paper, scissors)? "

    computerMove = choice( ["rock", "paper", "scissors"] )
    humanMove = input( questionWording )


    while humanMove != "rock" and humanMove != "paper" and humanMove != "scissors":
        
        print (humanMove + " IS NOT ONE OF THE CHOICES. YOU ARE A DOOR KNOB.  TRY AGAIN.")
        print("")
        humanMove = input( questionWording )

    
    print("")
    print ("Computer chose " + computerMove)

    #Decide who won
    if humanMove == computerMove:
        print("Tie")
        
    elif humanMove == "paper":
        if computerMove == "rock":
            print ('You won!')
            humScore += 1
        else:
            print ('You lost!')
            compScore += 1

    elif humanMove == "rock":
        if computerMove == "scissors":
            print ('You won!')
            humScore += 1
        else:
            print ('You lost!')
            compScore += 1

    else:
        if computerMove == "paper":
            print ('You won!')
            humScore += 1
        else:
            print ('You lost!')
            compScore += 1

print("")
if humScore == 3:
    print("You won the game! (" + str(humScore) + "-" + str(compScore) + ")")
else:
    print("The computer won. (" + str(compScore) + "-" + str(humScore) + ")")


