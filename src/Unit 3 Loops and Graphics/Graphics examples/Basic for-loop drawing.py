from tkinter import *
myInterface = Tk()
myScreen = Canvas(myInterface, width=1105, height=800, background="yellow")
myScreen.pack()

#Overlay a grid on the screen so you can see where the cooordinates lie
spacing = 100
for x in range(0, 800, spacing): 
    myScreen.create_line(x, 10, x, 800, fill="blue")
    myScreen.create_text(x, 0, text=str(x), font="Times 8", anchor = N)

for y in range(0, 800, spacing):
    myScreen.create_line(20, y, 800, y, fill="blue")
    myScreen.create_text(0, y, text=str(y), font="Times 8", anchor = W)


myScreen.update()


boxSize = 75

xUL = 100
yUL = 500

for i in range(0,10):

      xLR = xUL + boxSize
      yLR = yUL + boxSize

      myScreen.create_rectangle( xUL, yUL, xLR, yLR, fill="blue", outline="red", width=5)

      myScreen.update()
      xUL = xUL + boxSize
      
      

         
