from tkinter import *

#Creates a new tkinter window and assigns it to 'root'
root = Tk()

#Creates a new canvas widget with a parent window of 'root' and dimensions of 800x800
screen = Canvas(root, width = 800, height = 800)

#Places the canvas widget on its parent window
screen.pack()

#There are two more options for putting widgets on their parent window

#Option 1: .grid()

#screen.grid()

#Grid allows you to tell tkinter where on the window to place the widget
#by giving it a grid coordinate
#Best suited for when you have more than one widget that you want organized

#Option 2: .place()

#screen.place()

#Place allows you to tell tkinter exactly where to put the widget
#I don't recommend using place as its quite complicated

#Because in most cases you only  have the Canvas widget, I recomend
#continuing to use Pack
