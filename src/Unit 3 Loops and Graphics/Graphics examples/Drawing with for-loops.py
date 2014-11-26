from tkinter import *
myInterface = Tk()
myScreen = Canvas(myInterface, width=1105, height=800, background="yellow")
myScreen.pack()

xUL = 0
yUL = 800

boxSize = 200

for boxCounter in range(1,11):
    xUL = xUL + 40
    yUL = yUL - 50

    xLR = xUL + boxSize
    yLR = yUL + boxSize

    print(xUL, xLR)
    
    myScreen.create_rectangle( xUL, yUL, xLR, yLR, fill="blue")

    myScreen.update()
    
