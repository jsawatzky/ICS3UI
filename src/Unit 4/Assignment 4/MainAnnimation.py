'''
Created on Oct 29, 2014

@author: Jacob Sawatzky
'''
from tkinter import *
from utilities import *
from random import choice
from threading import Thread
from queue import Queue, Empty
from time import sleep

from sky import Sky
from sun import Sun
from moon import Moon
from clouds import Clouds
from ground import Ground

class MainThread(Thread):
    
    def __init__(self, queue):
        
        Thread.__init__(self)
        self.daemon = True
        
        self.queue = queue
        
    def run(self):
        
        sky = Sky(self.queue)
        sun = Sun(self.queue, 300, 100)
        moon = Moon(self.queue, 300, 100)
        #clouds = Clouds(self.queue, self)
        ground = Ground(self.queue)
        
        self.time = 75
        day = 0
        seasons = ["spring", "summer", "fall", "winter"]
        season = "spring"
        seasonStages = ["early", "mid", "mid", "late"]
        seasonStage = "mid"
        
        weatherOptions = ["clear", "clear", "clear", "clear", "cloudy", "cloudy", "overcast", "rain", "rain", "storm"]
        weather = "clear"
        
        while True:
            
            sky.update(self.time)
            sun.update(self.time)
            moon.update(self.time, day)
            ground.update(self.time, season, seasonStage, seasons)
            
            sun.draw()
            moon.draw()
            ground.draw()
                   
            self.time += 1
            if self.time > 1600:
                self.time = 0
                day += 1
                if day > 15:
                    day = 0
                season = seasons[int(day/4)]
                seasonStage = seasonStages[day%len(seasonStages)]
                
                if season == "winter" and seasonStage == "early":
                    weather = "rain"
                else: 
                    weather = choice(weatherOptions)
            
            sleep(0.01)
            
    def getTime(self):
        
        return self.time

##Functions
def run(tk):
    
    s = Canvas(tk, width =  800, height = 800, background = "blue")
    s.grid(row = 0, column = 0)
    
    queue = Queue()
    
    main = MainThread(queue)
    main.start()
    
    while True:
        
        try:
            task = queue.get(block = False)
        except Empty:
            pass
        else:
            try:
                if task.oper == "create":
                    object = s._create(task.object, task.coords, task.kw)
                    task.returnObject(object)
                elif task.oper == "config":
                    s.config(task.kw)
                elif task.oper == "coords":
                    s.coords(task.object, task.coords)
                elif task.oper == "itemconfig":
                    s.itemconfig(task.object, task.kw)
            except:
                break
        
        try:        
            tk.update()
        except:
            break
        
#Runs the program if not from menu
if __name__ == "__main__":
    run(Tk())
