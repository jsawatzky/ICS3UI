from tkinter import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="white")
screen.pack()

def drawCircle( xC, yC, r ): #parameters of drawCircle
    screen.create_oval(xC-r, yC-r, xC+r, yC+r, fill="yellow")
    screen.update()

drawCircle(0, 0, 100) #procedure call
    
