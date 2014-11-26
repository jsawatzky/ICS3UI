print("Welcome to my quiz! If you need a hint on any question, type \"hint\" as your answer \n")

q1 = "What is Mr. Schattman's favourite video game? "
q2 = "What is 8 x 5? "
q3 = "Which assignment are Janaki, Zack, Roman, Abdu, Walid, Jack and Abdurahim going to turn in by midnight tonight?"

questions = [q1, q2, q3]
numQuestions = len( questions )


#YOU FILL THIS OUT
correctAnswers = ["World of Peacecraft", "40", "3B"]
hints = ["It's the opposite of World of Warcraft", "It's more than 39 but less than 41", "It comes after 3A"]

userAnswers = []



#THE USER TAKES THE QUIZ
for i in range (0, numQuestions ):
    thisGuess = input( questions[i] )

    while thisGuess == "hint":
        print( hints[i] + "\n" )
        thisGuess = input( questions[i] )
        
    userAnswers.append( thisGuess )

print("\n")


#MARK THE QUIZ  
score = 0

for i in range (0, numQuestions ):
    
    questionNumber = i+1

    if userAnswers[i] == correctAnswers[i]:
        print("You got question #" + str(questionNumber) + " right!")
        score = score + 1

    else:
        print("You got question #" + str(questionNumber) + " WRONG!  The correct answer was: " + correctAnswers[i])

 
print("\nYour score is " + str(score) + " out of " + str( numQuestions ) )
