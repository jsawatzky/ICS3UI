'''
Created on Sep 30, 2014

@author: Jacob
'''

from tkinter import *
from utilities import *

myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="black")
s.pack()

x = 100
y = 700

length = 600

s.create_line(x, x + length, fill = "blue")
s.create_line(y, y - length, fill = "blue")

