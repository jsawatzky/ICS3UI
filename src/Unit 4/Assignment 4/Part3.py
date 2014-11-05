'''
Created on Oct 29, 2014

@author: Jacob Sawatzky
'''
from tkinter import *
from utilities import *
from random import choice

#Classes
class Sun():
    
    def __init__(self, startY, peak):
        self.k = peak
        self.h = 400
        self.a = (startY - self.k)/(self.h**2)
        self.object = None
        
    def update(self, time):
        if time > 1525:
            time -= 1600
        self.x = time
        self.y = self.a*((time-self.h)**2) + self.k
        
    def draw(self, s):
        if self.object == None:
            self.object = s.create_oval(self.x-75, self.y-75, self.x+75, self.x+75, fill = "yellow", outline = "yellow")
        else:
            s.coords(self.object, self.x-75, self.y-75, self.x+75, self.y+75)
            
class Moon():
    
    def __init__(self, startY, peak):
        self.k = peak
        self.h = 400
        self.a = (startY - self.k)/(self.h**2)
        self.object = None
        
    def update(self, time):
        time -= 800
        if time < -50:
            time += 1600
        self.x = time
        self.y = self.a*((time-self.h)**2) + self.k
        
    def draw(self, s):
        if self.object == None:
            self.object = s.create_oval(self.x-50, self.y-50, self.x+50, self.x+50, fill = "white", outline = "white")
        else:
            s.coords(self.object, self.x-50, self.y-50, self.x+50, self.y+50)
            
class Sky():
    
    def __init__(self):
        colors = {}
        colors['sunrise'] = "#FFC012"
        colors['sunset'] = "#DE8501"
        colors['day'] = "#3AA0FF"
        colors['night'] = "#121C43"
        self.colors = colors
        
    def update(self, s, time):
        if 0 <= time < 75 or 725 <= time < 800:
            color = self.colors['sunrise'] 
        elif 75 <= time < 725:
            color = self.colors['day']
        elif 800 <= time < 875 or 1525 <= time < 1600:
            color = self.colors['sunset']
        else:
            color = self.colors['night']
        s.config(background = color)

##Functions
def run(tk):
    
    s = Canvas(tk, width =  800, height = 800, background = "blue")
    s.grid(row = 0, column = 0)
    
    sky = Sky()
    sun = Sun(300, 100)
    moon = Moon(300, 100)
    
    time = 0
    day = 1
    seasons = ["spring", "summer", "fall", "winter"]
    season = "spring"
    seasonStages = ["early", "mid", "mid", "late"]
    seasonStage = 0
    
    weatherOptions = ["clear", "clear", "clear", "overcast", "rain", "storm"]
    weather = 0
    
    while True:
        
        sky.update(s, time)
        sun.update(time)
        moon.update(time)
        
        sun.draw(s)
        moon.draw(s)
        
        s.update()
               
        time += 1
        if time > 1600:
            time = 0
            day += 1
            if day > 16:
                day = 1
            season = seasons[int((day-1)/4)]
            seasonStage = seasonStages[(day-1)%len(seasonStages)]
                    
            weather = choice(weatherOptions)
        
        pause(0.01, tk)
    
    clearScreen(tk)
        
#Runs the program if not from menu
if __name__ == "__main__":
    run(Tk())