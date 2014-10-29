'''
Created on Oct 6, 2014

@author: sawaj6311
'''

from random import *
from threading import Thread
from time import sleep
from tkinter import *

#from utilities import *


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
#grid(s, 25)

#Command and button to close window
def buttonCmd():
    global running, myInterface
    running = False
    myInterface.destroy()
button = Button(s, text="Done", command = buttonCmd)
button.configure(width = 10, activebackground = "green")
s.create_window(710, 760, anchor = NW, window = button)

#Variables
time = 19 #0-18 = sunrise, 19-181 = day, 182-218 = sunset, 219-381 = night, 382-400 = sunrise
season = 0 #0-2 = spring, 3-5 = summer, 6-8 = fall, 9-11 = winter
weather = 0 #0 = clear, 1 = cloudy, 2 = overcast, 3 = rain/snow

sky = {}
sky['sunrise1'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#DE8501")
sky['sunrise2'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#FFC012")
sky['day'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#3AA0FF")
sky['sunset1'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#FFC012")
sky['sunset2'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#DE8501")
sky['night'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#121C43")
stars = []
for star in range(0, 60):
    stars.append({})
    stars[star]['x'] = randint(0, 790)
    stars[star]['y'] = randint(0, 390)
    stars[star]['size'] = randint(2, 5)
    stars[star]['i'] = s.create_oval(-5000, -5000, -5000, -5000, fill = "white", outline = "white")
starIndex = 0
asteriods = [] #TODO
sun = s.create_oval(-5000, -5000, -5000, -5000, fill = "yellow", outline = "yellow")
sunSize = 75
moon = s.create_oval(-5000, -5000, -5000, -5000, fill = "black", outline = "black")
moonSize = 50
clouds = []
for cloud in range(0, 21):
    clouds.append(s.create_oval(-5000, -5000, -5000, -5000, fill="white", outline="white"))
cloudIndex = 0
ground = {}
ground['spring'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#01A611")
ground['summer'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#005C09")
ground['fall'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#007B0C")
ground['winter'] = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "white")
tree = [] #TODO
flowers = [] #TODO
grass = [] #TODO
rain = [] #TODO

inUpdate = False

def update():
    global s, time, season, weather, sun, sunSize, moon, moonSize, clouds, cloudIndex, stars, starIndex, asteriods, rain, ground, grass, tree, flowers, inUpdate
    
    inUpdate = True
    
    #Main animation
    #Sky
    if time == 0:
        s.coords(sky['sunrise1'], -5000, -5000, -5000, -5000)
        s.coords(sky['sunrise2'], 0, 0, 800, 400)
    elif time == 19:
        s.coords(sky['sunrise2'], -5000, -5000, -5000, -5000)
        s.coords(sky['day'], 0, 0, 800, 400)
    elif time == 182:
        s.coords(sky['day'], -5000, -5000, -5000, -5000)
        s.coords(sky['sunset1'], 0, 0, 800, 400)
    elif time == 200:
        s.coords(sky['sunset1'], -5000, -5000, -5000, -5000)
        s.coords(sky['sunset2'], 0, 0, 800, 400)
    elif time == 219:
        s.coords(sky['sunset2'], -5000, -5000, -5000, -5000)
        s.coords(sky['night'], 0, 0, 800, 400)
    elif time == 382:
        s.coords(sky['night'], -5000, -5000, -5000, -5000)
        s.coords(sky['sunrise1'], 0, 0, 800, 400)
        
    #Stars
    if 219 <= time <= 248:
        for star in range(starIndex, starIndex + 2):
            star = stars[star]
            s.coords(star['i'], star['x'] , star['y'], star['x']+star['size'], star['y']+star['size'])
        starIndex += 2
        if starIndex == 60:
            starIndex = 0
    elif 351 < time < 382:
        for star in range(starIndex, starIndex + 2):
            star = stars[star]
            s.coords(star['i'], -5000, -5000, -5000, -5000)
        starIndex += 2
        if starIndex == 60:
            starIndex = 0
    
    #Sun and moon
    sunX = time*4
    if sunX > 800+sunSize:
        sunX -= 1600
    sunY = (0.000625)*((sunX-400)**2) + 100
    s.coords(sun, sunX-sunSize, sunY-sunSize, sunX+sunSize, sunY+sunSize)
    moonX = (time-200)*4
    if moonX < -moonSize:
        moonX += 1600
    moonY = (0.000625)*((moonX-400)**2) + 100
    s.coords(moon, moonX-moonSize, moonY-moonSize, moonX+moonSize, moonY+moonSize)
    
    #Weather ANIMATE CLOUDS!!!
    if weather == 0:
        if time % 10 == 0 and time < 71:
            for cloud in range(cloudIndex, cloudIndex+3):
                s.coords(clouds[cloud], -5000, -5000, -5000, -5000)
            cloudIndex += 3
            if cloudIndex == 21:
                cloudIndex = 0
    elif weather == 1:
        if time % 10 == 0 and time < 71:
            x = randint(0,760)
            for cloud in range(cloudIndex, cloudIndex+3):
                x1 = x+randint(-75, 75)
                s.coords(clouds[cloud], x1, -20, x1+randint(100,150), randint(40,100))
                s.itemconfig(clouds[cloud], fill = "white", outline = "white")
            cloudIndex += 3
            if cloudIndex == 21:
                cloudIndex = 0
    if weather >= 2:
        if time % 10 == 0 and time < 71:
            x = randint(0,760)
            for cloud in range(cloudIndex, cloudIndex+3):
                x1 = x+randint(-75, 75)
                s.coords(clouds[cloud], x1, -20, x1+randint(100,150), randint(40,100))
                s.itemconfig(clouds[cloud], fill = "grey", outline = "grey")
            cloudIndex += 3
            if cloudIndex == 21:
                cloudIndex = 0
                
    #Ground
    if season < 3:
        s.coords(ground['winter'], -5000, -5000, -5000, -5000)
        s.coords(ground['spring'], 0, 400, 800, 800)
    elif season < 6:
        s.coords(ground['spring'], -5000, -5000, -5000, -5000)
        s.coords(ground['summer'], 0, 400, 800, 800)
    elif season < 9:
        s.coords(ground['summer'], -5000, -5000, -5000, -5000)
        s.coords(ground['fall'], 0, 400, 800, 800)
    elif season < 12:
        s.coords(ground['fall'], -5000, -5000, -5000, -5000)
        s.coords(ground['winter'], 0, 400, 800, 800)
    
    time += 1
    if time == 401:
        time = 0
        season += 1
        if season == 12:
            season = 0
        weather = randint(0, 3)
    
    s.update()
    
    inUpdate = False

#Update thread
class UpdateThread(Thread):

    def run(self):
        global running
        while running == True:
            update()
            sleep(0.05)

updateThread = UpdateThread()
updateThread.start()

while running == True:
    if inUpdate == False:
        s.update()