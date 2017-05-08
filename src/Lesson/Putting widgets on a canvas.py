from tkinter import *

root = Tk()

screen = Canvas(root, width = 400, height = 400, bg = "white")
screen.pack()

#Create the widget using the canvas as its parent now
button = Button(screen, text = "Button in a canvas!", command = lambda: print("Hello world!"))

#Use 'screen.create_window() to place the widget on the screen
screen.create_window(300, 270, window = button)
