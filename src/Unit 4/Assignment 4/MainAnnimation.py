'''
Created on Oct 29, 2014

@author: Jacob Sawatzky
'''
from tkinter import *
from utilities import *
from random import choice
from multiprocessing import *
from time import sleep

from sky import Sky
from sun import Sun
from moon import Moon
from clouds import Clouds
from ground import Ground

class MainThread(Process):
    
    def __init__(self, queue, shared):
        
        Process.__init__(self)
        self.daemon = True
        
        self.queue = queue
        self.shared = shared
        
    def run(self):
        
        sky = Sky(self.queue)
        sun = Sun(self.queue, 300, 100)
        moon = Moon(self.queue, 300, 100)
        ground = Ground(self.queue)
        
        time = 75
        self.shared[0] = time
        day = 0
        seasons = ["spring", "summer", "fall", "winter"]
        season = "spring"
        seasonStages = ["early", "mid", "mid", "late"]
        seasonStage = "mid"
        
        weatherOptions = ["clear", "clear", "clear", "clear", "cloudy", "cloudy", "overcast", "rain", "rain", "storm"]
        weather = "clear"
        self.shared[1] = weatherOptions.index(weather)
        
        while True:
            
            sky.update(time)
            sun.update(time)
            moon.update(time, day)
            ground.update(time, season, seasonStage, seasons)
            
            sun.draw()
            moon.draw()
            ground.draw()
                   
            time += 3
            if time > 1600:
                time = 0
                day += 1
                if day > 15:
                    day = 0
                season = seasons[int(day/4)]
                seasonStage = seasonStages[day%len(seasonStages)]
                
                if season == "winter" and seasonStage == "early":
                    weather = "rain"
                else: 
                    weather = choice(weatherOptions)
                print(weather)
            
            self.shared[0] = time
            self.shared[1] = weatherOptions.index(weather)
            sleep(0.05)

##Functions
def run(tk):
    
    s = Canvas(tk, width =  800, height = 800, background = "blue")
    s.grid(row = 0, column = 0)
    
    queue = Queue()
    
    shared = Array('i', [0, 0])
    
    main = MainThread(queue, shared)
    main.start()
    clouds = Clouds(queue, shared)
    clouds.start()
    
    while True:
        
        try:
            task = queue.get(block = False)
        except:
            pass
        else:
            try:
                if task.oper == "create":
                    object = s._create(task.object, task.coords, task.kw)
                    task.pipeSend.send(object)
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
