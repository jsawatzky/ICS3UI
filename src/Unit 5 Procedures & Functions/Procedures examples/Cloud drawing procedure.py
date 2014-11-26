from tkinter import *
from time import *
from random import *
root = Tk()
screen = Canvas(root, width = 800, height = 800, background = "sky blue")
screen.pack()


def drawCloud(xCentre, yCentre, maxWidth, maxHeight, numOvals):
      
      for i in range(1,numOvals+1):
            xUL = xCentre - randint(1, maxWidth)
            yUL = yCentre - randint(1, maxHeight)
            xLR = xCentre + randint(1, maxWidth)
            yLR = yCentre + randint(1, maxHeight)
            oval = screen.create_oval(xUL, yUL, xLR, yLR, fill="white", outline="white")
            
      screen.update()


##drawCloud(400, 570, 300, 10, 3 )
##drawCloud(200, 200, 100, 50, 300)
###drawCloud(100, 500, 100, 50)


###Fill the sky with clouds
for cloudNum in range(1,20):
      
      xCentre = randint(0,800)
      yCentre = randint(0,800)
      maxWidth = randint(40,150)
      maxHeight = randint(20,75)
      
      drawCloud( xCentre, yCentre, maxWidth, maxHeight, 30)


      
