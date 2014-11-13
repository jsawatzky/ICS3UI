'''
Created on Nov 12, 2014

@author: Jacob
'''
from utilities import *
from multiprocessing import *
from time import sleep
from random import randint
from tkinter.constants import NORMAL, HIDDEN

class Rain(Process):
    
    def __init__(self, queue, shared, paused):
        
        Process.__init__(self)
        self._daemonic = True
        
        self.queue = queue
        self.shared = shared
        self.paused = paused
        
        self.weatherOptions = ["clear", "clear", "clear", "clear", "cloudy", "cloudy", "overcast", "rain", "rain", "storm"]
        self.seasons = ["spring", "summer", "fall", "winter"]
        
    def update(self):
            
        if self.weatherOptions[self.shared[1]] == "storm":
            windSpeed = 4
        else:
            windSpeed = 2
                
        for i in range(len(self.rain)):
            
            self.rain[i]['x'] += windSpeed
            self.rain[i]['y'] += self.rain[i]['speed']
            
            if self.rain[i]['y'] > 800:
                self.rain[i]['x'] = randint(-300, 700)
                self.rain[i]['y'] = -10
                
                if self.weatherOptions[self.shared[1]] == "rain" or self.weatherOptions[self.shared[1]] == "storm":
                    self.queue.put(QueueItem("itemconfig", self.rain[i]['object'], state = NORMAL))
                else:
                    self.queue.put(QueueItem("itemconfig", self.rain[i]['object'], state = HIDDEN))
                    
                if self.seasons[self.shared[2]] == "winter":
                    self.queue.put(QueueItem("itemconfig", self.rain[i]['object'], fill = "white", outline = "white"))
                else:
                    self.queue.put(QueueItem("itemconfig", self.rain[i]['object'], fill = "blue", outline = "blue"))
                    
            self.queue.put(QueueItem("coords", self.rain[i]['object'], self.rain[i]['x']-self.rain[i]['size'], self.rain[i]['y']-self.rain[i]['size'], self.rain[i]['x']+self.rain[i]['size'], self.rain[i]['y']+self.rain[i]['size']))
    
    def run(self):
        
        while self.paused[3] == 1:
            pass
        
        self.rain = []
        for i in range(300):
            
            self.rain.append({})
            x = randint(-800, 700)
            y = randint(-800, -10)
            size = randint(2, 4)
            color = "blue"
            self.rain[i]['x'] = x
            self.rain[i]['y'] = y
            self.rain[i]['size'] = size
            self.rain[i]['speed'] = randint(4, 6)
            weather = self.weatherOptions[self.shared[1]]
            print(weather)
            if weather == "rain" or weather == "storm":
                queueItem = QueueItem("create", 'oval', x-size, y-size, x+size, y+size, fill = color, outline = color, state = NORMAL)
            else:
                queueItem = QueueItem("create", 'oval', x-size, y-size, x+size, y+size, fill = color, outline = color, state = HIDDEN)
            self.queue.put(queueItem)
            self.rain[i]['object'] = None
            while self.rain[i]['object'] == None:
                self.rain[i]['object'] = queueItem.pipeRecv.recv()
        
        self.queue.put(QueueItem("cont"))   
        self.paused[3] = 1
        self.paused[1] = 0
        while self.paused[3] == 1:
            pass
        
        while True:
            self.update()
            self.queue.put(QueueItem("cont"))
            self.paused[3] = 1
            sleep(0.05)
            while self.paused[3] == 1:
                pass
        
        