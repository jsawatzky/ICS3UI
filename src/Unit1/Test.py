'''
Created on Sep 9, 2014

@author: Jacob
'''

from turtle import *
from math import *

t = Pen()

t.seth(0)

for i in range(0, 1024):
    t.goto(i*20, 20*sin(i))