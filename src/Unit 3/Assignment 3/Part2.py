'''
Created on Sep 30, 2014

@author: Jacob
'''

from tkinter import *
from utilities import *

WIDTH = 800
HEIGHT = 800

myInterface = Tk()
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="black")
s.pack()

x = 100
y = HEIGHT-100

length = min(WIDTH, HEIGHT)-200

s.create_line(x, y, x + length, y, fill = "blue")
s.create_line(x, y, x, y - length, fill = "blue")

text1 = s.create_text(WIDTH/2, (HEIGHT/2)-30, text = "How many lines would you like?", fill = "white", anchor = N)

numLines = 0

entry = Entry(s)
entry.configure(width = 20)
entry.insert(0, str(int(length/5)))
s.create_window((WIDTH/2)+7, HEIGHT/2, window = entry, anchor = E)

def setNumLines():
    global entry, numLines, text2
    numLines = entry.get()
    if numLines > length/2:
        numLines = 0
        text2 = s.create_text(WIDTH/2, (HEIGHT/2)+30, text = "Please enter a number less than " + str(int(length/2)), fill = "white", anchor = S)
    elif numLines <= 0:
        numLines = 0
        text2 = s.create_text(WIDTH/2, (HEIGHT/2)+30, text = "Please enter a number greater than 0", fill = "white", anchor = S)
    else:
        entry.destroy()
        button.destroy()
        s.delete(text1, text2)

button = Button(s, text="Enter", command = setNumLines, anchor = W)
button.configure(width = 10, activebackground = "green")
s.create_window((WIDTH/2)+3, HEIGHT/2, window = button, anchor = W)

while True:
    s.update()