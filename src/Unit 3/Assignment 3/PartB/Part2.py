'''
Created on Oct 14, 2014

@author: Jacob Sawatzky
'''

from tkinter import *

WIDTH = 400
HEIGHT = 800

tk = Tk()
s = None
label = Label(tk, text = "How many rows of fractions do you want?")
entry = Entry(tk)
numRows = 0
def setNumRows():
    global WIDTH, HEIGHT, tk, label, entry, button, errorLabel, numRows
    try:
        numLines = int(entry.get())
        if numLines == 0:
            raise ValueError
    except ValueError:
        errorLabel = Label(tk, text = "You must enter an integer!")
        errorLabel.grid(row = 2)
    else:
        if numLines > WIDTH/10:
            WIDTH = numLines*10
        if numLines > HEIGHT/20:
            HEIGHT = numLines*20
        label.destroy()
        entry.destroy()
        button.destroy()
        if errorLabel != None:
            errorLabel.destroy()
button = Button(tk, text = "Enter", command = setNumRows)
errorLabel = None

def drawBoxes():
    global s, WIDTH, HEIGHT, numRows
    
    
    
def run():
    global s, WIDTH, HEIGHT
    
    while numRows == 0:
        pass
    
    s = Canvas(tk, width=WIDTH, height=HEIGHT, bg = "black")
    s.grid(row = 0, column = 0)
    
    drawBoxes()