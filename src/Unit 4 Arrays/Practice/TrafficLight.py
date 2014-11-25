'''
Created on Oct 28, 2014

@author: Jacob Sawatzky
'''

from tkinter import *
from time import sleep

tk = Tk()
s = Canvas(tk, width = 300, height = 900, background = "Orange")
s.pack()

colors = [["red", "Dark Orange", "Dark Green"], ["Dark Red", "yellow", "Dark Green"], ["Dark Red", "Dark Orange", "green"]]
colors.reverse()

red = s.create_oval(25, 25, 275, 275, fill = "Dark Red")
yellow = s.create_oval(25, 325, 275, 575, fill = "Dark Orange")
green = s.create_oval(25, 625, 275, 875, fill = "Dark Green")

i = 0

while True:
    
    colorSet = colors[i%3]
    
    red = s.create_oval(25, 25, 275, 275, fill = colorSet[0])
    yellow = s.create_oval(25, 325, 275, 575, fill = colorSet[1])
    green = s.create_oval(25, 625, 275, 875, fill = colorSet[2])
    
    s.update()
    sleep(2)
    
    i += 1