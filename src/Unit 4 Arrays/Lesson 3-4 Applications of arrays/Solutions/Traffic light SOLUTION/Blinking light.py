from tkinter import *
from time import *


root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()


#BLINKING LIGHTS ANIMATION

lightColors = ["green", "yellow", "red"]

for i in range(0, 200):

    screen.create_oval(450,400,550,500, fill = lightColors[ i % 3 ] )
    
    screen.update()
    sleep(0.2)
    
    
