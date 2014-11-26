from tkinter import *
from random import *

myInterface = Tk()
s = Canvas(myInterface, width=600, height=600, background="black")
s.pack()


#DEFINE THE NEW PROCEDURE. IT TAKES ONE PARAMETER
def drawStarCluster( starColor, numStars ):
    for i in range(0, numStars):
        x = randint(0,600)
        y = randint(0,600)
        size = randint(1,6)
        s.create_oval(x, y, x+size, y+size, fill= starColor)
        s.update()


#CALL THE PROCEDURE WITH ARGUMENT "white"
drawStarCluster( "white", 100 )


#CALL THE PROCEDURE WITH A DIFFERENT ARGUMENT
drawStarCluster( "yellow", 20  )

drawStarCluster( "red", 49 )


