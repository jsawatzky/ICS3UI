#PLAYS ROCK PAPER SCISSORS ONLY ONCE, BUT MAKES SURE THE USER
#ENTERS A VALID CHOICE

from random import *

for i in range(1,5):
    
    questionWording = "What move would you like to pick (rock, paper, scissors)? "

    computerMove = choice( ["rock", "flame thrower", "scissors"] )
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
        else:
            print ('You lost!')

    elif humanMove == "rock":
        if computerMove == "scissors":
            print ('You won!')
        else:
            print ('You lost!')

    else:
        if computerMove == "paper":
            print ('You won!')
        else:
            print ('You lost!')


