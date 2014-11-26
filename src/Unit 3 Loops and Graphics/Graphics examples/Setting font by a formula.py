from tkinter import *
root = Tk()
screen = Canvas(root, width=1000, height=800, background = "white" )
screen.pack()

yPos = 20

for wordCount in range( 1, 15 ):
    
    yPos = yPos + 50
    fontSize = 3*wordCount
    screen.create_text( 400, yPos, text = "ICS3UI", font = "Times " + str(fontSize), fill = "blue")

screen.update()
