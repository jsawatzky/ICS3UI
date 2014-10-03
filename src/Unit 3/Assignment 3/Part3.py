'''
Created on Oct 2, 2014

@author: Jacob
'''

from tkinter import *
from time import sleep
from utilities import *

#Boolean for update loops
running = True

#Constants for reference
WIDTH = 800
HEIGHT = 800

#Creates the screen
myInterface = Tk()
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="white")
s.pack()

#Draws grid
grid(s, 25)

#Command and button to close window
def buttonCmd():
    global running, myInterface
    running = False
    myInterface.destroy()
button = Button(s, text="Done", command = buttonCmd)
button.configure(width = 10, activebackground = "green")
s.create_window(710, 760, anchor = NW, window = button)

#Variables
time = 0 #0-100 = day, 101-200 = night
season = 0 #0-200 = spring, 201-400 = summer, 401-600 = fall, 601-800 = winter
weather = 0 #0 = clear, 1 = rain/snow

sun = None
sunSize = 75
clouds = []
stars = []
asteriods = []
rain = []
ground = None
grass = []
tree = []
flowers = []

def update():
    global s, time, season, weather, sun, sunSize, clouds, stars, asteriods, rain, ground, grass, tree, flowers
    #Main animation
    if time < 101:
        s.delete(sun)
        sunY = (0.000625)*((time*8-400)**2) + 100
        sun = s.create_oval(time*8-sunSize, sunY-sunSize, time*8+sunSize, sunY+sunSize, fill = "yellow")
    
    time += 1
    if time == 201:
        time = 0
    
    s.update()
    sleep(0.01)

#Update loop
while running == True:
    try:
        update()
    except:
        running = False