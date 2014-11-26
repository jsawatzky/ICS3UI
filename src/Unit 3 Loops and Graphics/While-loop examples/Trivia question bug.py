#ASK A TRIVIA QUESTION
yourGuess = input("Who's the coolest CS teacher at SJAM?")


#ASK REPEATEDLY UNTIL THE USER ENTERS ONE OF THE TWO ACCEPTABLE ANSWERS
#BUT THERE'S A LOGIC ERROR HERE...CAN YOU FIND IT?
                               
while yourGuess != "Mr. Schattman" or yourGuess != "Mr. S":
      
      yourGuess = input("Wrong. Guess again: ")


#PRINT A RESPONSE WHEN THE LOOP QUITS
print("Right! Because he's the only CS teacher at SJAM!")
