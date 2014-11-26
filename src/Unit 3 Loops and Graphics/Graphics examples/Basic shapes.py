###############################################################
# This program shows how to draw things on the screen in Python
###############################################################

#Import the tkinter module, which has functions for making graphical user interfaces
from tkinter import *
myInterface = Tk()
myScreen = Canvas(myInterface, width=800, height=800, background="turquoise")
myScreen.pack()

#Create some rectangles
myScreen.create_rectangle( 200,   0, 400, 800, fill = "red")
myScreen.create_rectangle( 100, 100, 300, 300, fill = "green")
myScreen.create_rectangle( 200, 200, 300, 300, fill = "yellow")

#Create an oval with upper-left corner at (500, 300) and lower-right corner at (600,350)
myScreen.create_rectangle( 500, 300, 600, 350, fill = "purple", outline="red", width = 3)
myScreen.create_oval( 500, 300, 600, 350, fill = "black", outline="red", width = 3)

#Create a polygon that connects the points (400,400), (450,500), (400,450), (350,500) and back to (400, 400).
myScreen.create_polygon( 400,400, 450,500,400,450,350,500, 2, 1, 400, 400, fill="green",outline="hot pink",width=3)

#Write a message
myScreen.create_text( 300, 500, text="ICS3UI Rocks!", font="Times 30 italic bold", fill = "black")


#Actually place the new graphics created above onto the canvas
myScreen.update()


#Overlay a grid on the screen so you can see where the cooordinates lie
spacing = 100
for x in range(0, 800, spacing): 
    myScreen.create_line(x, 10, x, 800, fill="blue")
    myScreen.create_text(x, 0, text=str(x), font="Times 8", anchor = N)

for y in range(0, 800, spacing):
    myScreen.create_line(20, y, 800, y, fill="blue")
    myScreen.create_text(0, y, text=str(y), font="Times 8", anchor = W)



