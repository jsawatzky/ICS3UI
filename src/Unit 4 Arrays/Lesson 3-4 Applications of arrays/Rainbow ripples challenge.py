from tkinter import *
from time import *

tk = Tk()
me = Canvas(tk, width=800,height=800,background="black")
me.pack()

xCentre = 400
yCentre = 400

xLimit = 700

rippleColors = ["red", "blue", "yellow", "green", "blue", "purple"]

speed = 5

gap = 10

rippleNum = 0

while xLimit > 0:

    # reset the starting position of the next ripple
    x1 = xCentre
    y1 = yCentre
    
    x2 = xCentre
    y2 = yCentre

    # animate the next ripple
    while x2 < xLimit:

        x1 = x1 - speed
        y1 = y1 - speed
        x2 = x2 + speed
        y2 = y2 + speed

        ripple = me.create_oval(x1, y1, x2, y2, outline = "yellow", width=9 )
        
        me.update()
        sleep(0.001)

        #Keep the very last frame in each ripple
        if x2 < xLimit:  
            me.delete(ripple)

            
    # reduce xLimit so that the next ripple is smaller than the last one
    xLimit = xLimit - gap  


# wipe the slate clean with a solid, black ripple
sleep(2)

x1 = xCentre
y1 = yCentre

x2 = xCentre
y2 = yCentre

speed = 3

while x2 < 900: 

        x1 = x1 - speed
        y1 = y1 - speed
        x2 = x2 + speed
        y2 = y2 + speed

        me.create_oval(x1, y1, x2, y2, fill = "black", outline="red", width=4)
        me.update()
        sleep(0.005)
        
 
        

