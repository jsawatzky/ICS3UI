#Experiment with this a few times
#Exercise: make it draw a rainbow octagon with 8 different colours

import turtle
jessica = turtle.Pen()

myLength = 10

jessica.width(3)
jessica.speed(2)
colorChoices = ["red", "blue", "green", "black"]

for lineCounter in range(0, 50):

    colorNumber = lineCounter % 4   
    jessica.color( colorChoices[ colorNumber ] )

    jessica.forward( myLength )
    jessica.left( 122 )

    myLength = myLength + 4

    


