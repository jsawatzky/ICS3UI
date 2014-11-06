'''
Created on Oct 29, 2014

@author: Jacob Sawatzky
'''
from tkinter import *
from utilities import *
from random import choice

def getColor(startColor, endColor, startTime, endTime, time):
        
    startRed = startColor[0]
    startGreen = startColor[1]
    startBlue = startColor[2]
    endRed = endColor[0]
    endGreen = endColor[1]
    endBlue = endColor[2]
        
    red = (startRed * (endTime - time) + endRed * (time - startTime)) / (endTime - startTime)
    green = (startGreen * (endTime - time) + endGreen * (time - startTime)) / (endTime - startTime)
    blue = (startBlue * (endTime - time) + endBlue * (time - startTime)) / (endTime - startTime)
        
    color = "#%02x%02x%02x" % (red, green, blue)
        
    return color

#Classes
class Sky():
    
    def __init__(self):
        colors = {}
        colors['sunrise'] = [255, 192, 18]
        colors['sunset'] = [222, 133, 1]
        colors['day'] = [58, 160, 255]
        colors['night'] = [18, 28, 67]
        self.colors = colors
        
        
    def update(self, s, time):
        
        colors = self.colors
        
        if time in range(0, 26):
            tempColors = []
            for i in range(0, 3):
                tempColors.append((colors['sunset'][i]+colors['sunrise'][i])/2)
            color = getColor(tempColors, colors['sunrise'], 0, 25, time)
        elif time in range(26, 76):
            color = getColor(colors['sunrise'], colors['day'], 26, 75, time)
        elif time in range(76, 726):
            color = "#3AA0FF"
        elif time in range(726, 776):
            color = getColor(colors['day'], colors['sunrise'], 726, 775, time)
        elif time in range(776, 826):
            color = getColor(colors['sunrise'], colors['sunset'], 776, 825, time)
        elif time in range(826, 876):
            color = getColor(colors['sunset'], colors['night'], 826, 875, time)
        elif time in range(876, 1526):
            color = "#121C43"
        elif time in range(1526, 1576):
            color = getColor(colors['night'], colors['sunset'], 1526, 1576, time)
        elif time in range(1576, 1601):
            tempColors = []
            for i in range(0, 3):
                tempColors.append((colors['sunset'][i]+colors['sunrise'][i])/2)
            color = getColor(colors['sunset'], tempColors, 1576, 1600, time)
            
        s.config(background = color)

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
        self.back = None
        self.front = None
        
    def update(self, s, time, day):
        time -= 800
        if time < -50:
            time += 1600
        self.x = time
        self.y = self.a*((time-self.h)**2) + self.k
        
        day %= 8
        
        if day < 2 or day > 5:
            s.itemconfig(self.front, fill = "white", outline = "white")
            s.itemconfig(self.front, fill = "#121C43", outline = "#121C43")
        else:
            s.itemconfig(self.front, fill = "#121C43", outline = "#121C43")
            s.itemconfig(self.back, fill = "white", outline = "white")
            
        day %= 4
        
        if day == 0:
            pass
        elif day == 1:
            pass
        elif day == 2:
            pass
        else:
            pass
        
    def draw(self, s):
        if self.back == None:
            self.back = s.create_oval(self.x-50, self.y-50, self.x+50, self.x+50, fill = "#121C43", outline = "#121C43")
        if self.front == None:
            self.front = s.create_oval(self.x-50, self.y-50, self.x+50, self.x+50, fill = "white", outline = "white")
        
        s.coords(self.back, self.x-50, self.y-50, self.x+50, self.y+50)
        
class Ground():
    
    def __init__(self):
        pass

##Functions
def run(tk):
    
    s = Canvas(tk, width =  800, height = 800, background = "blue")
    s.grid(row = 0, column = 0)
    
    sky = Sky()
    sun = Sun(300, 100)
    moon = Moon(300, 100)
    
    time = 75
    day = 0
    seasons = ["spring", "summer", "fall", "winter"]
    season = "spring"
    seasonStages = ["early", "mid", "mid", "late"]
    seasonStage = 0
    
    weatherOptions = ["clear", "clear", "clear", "clear", "cloudy", "cloudy", "overcast", "rain", "storm"]
    weather = 0
    
    while True:
        
        sky.update(s, time)
        sun.update(time)
        moon.update(s, time, day)
        
        sun.draw(s)
        moon.draw(s)
        
        s.update()
               
        time += 1
        if time > 1600:
            time = 0
            day += 1
            if day > 15:
                day = 0
            season = seasons[int(day/4)]
            seasonStage = seasonStages[day%len(seasonStages)]
                    
            weather = choice(weatherOptions)
        
        pause(0.01, tk)
    
    clearScreen(tk)
        
#Runs the program if not from menu
if __name__ == "__main__":
    run(Tk())
