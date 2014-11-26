from tkinter import *
myInterface = Tk()
myScreen = Canvas(myInterface, width=1105, height=800, background="yellow")
myScreen.pack()

xUL = 200
yUL = 200
xLR = 600
yLR = 600

boxSize = 200

for boxCounter in range(1,11):
    xUL = xUL + 20
    yUL = yUL + 20

    xLR = xLR - 20
    yLR = yLR - 20

    #print(xUL, xLR)
    
    myScreen.create_rectangle( xUL, yUL, xLR, yLR, fill="red", outline="black")

    myScreen.update()
    
