from tkinter import *
from time import *

tk = Tk()
me = Canvas(tk, width=600, height=900, background="black")
me.pack()

colorChoices = [ "blue", "light blue", "red", "green", "yellow", "grey50", "hot pink" ]
numColors = len(colorChoices)

x1 = 100
x2 = x1 + 400

for i in range(0,22):
    y1 = i * 25
    y2 = y1 + 25

    myCurrentColor = colorChoices[ i % numColors ]  #cycling through an array

    print( i % numColors )
    
    me.create_rectangle( x1, y1, x2, y2, fill = myCurrentColor )
    
    me.update()
    sleep(0.4)
    
