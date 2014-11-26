from tkinter import *
from random import *
from time import *

myInterface = Tk()
myScreen = Canvas(myInterface, width=800, height=800, background="yellow")
myScreen.pack()

while True:
    delay = 1.5
    maximum = 0

    q = myScreen.create_text( 400, 400, text="Find the maximum...ready?", font="Times 48 bold", fill = "red")
    myScreen.update()

    sleep(2)

    myScreen.delete(q)
    
    sleep(1)

    for i in range( 1, 11 ):
        x = randint( 1, 3000 )
        
        if x > maximum:
            maximum=x
        
        xText = myScreen.create_text( 400, 400, text=str(x), font="Times 48 bold", fill = "blue")

        myScreen.update()
        sleep(delay)
        myScreen.delete(xText)


    sleep(1)

    q1 = myScreen.create_text( 400, 400, text="Did you get it?", font="Times 48 bold", fill = "red")
    myScreen.update()

    sleep(2)

    myScreen.delete(q1)

    q2 = myScreen.create_text( 400, 400, text="MAXIMUM: " + str(maximum), font="Times 48 bold", fill = "red")
    myScreen.update()
    
    sleep(2)

    myScreen.delete(q2)

    sleep(1)
    
