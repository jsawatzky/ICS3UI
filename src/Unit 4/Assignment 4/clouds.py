'''
Created on Nov 8, 2014

@author: Jacob
'''
from utilities import *
from time import *
from multiprocessing import *
from random import randint, shuffle, choice

class Clouds(Process):
    
    def __init__(self, queue, shared, paused):
        
        Process.__init__(self)
        self._daemonic = True
        
        self.queue = queue
        self.shared = shared
        self.paused = paused
        
        self.weatherOptions =  ["clear", "clear", "clear", "clear", "cloudy", "cloudy", "overcast", "rain", "rain", "storm"]
        
    def resetCloud(self, cloud):
        
        width = randint(175, 250)
        if self.oldWeather == "clear":
            cloud['x'] = randint(-800-width, -width)
        else:
            cloud['x'] = -width
        cloud['y'] = randint(-5, 20)
        cloud['width'] = width
        cloud['speed'] = randint(5, 8)
        for o in range(3):
            width2 = randint(100, 175)
            cloud['objects'][o]['x'] = randint(-width+width2, width-width2)
            cloud['objects'][o]['y'] = randint(-5, 20)
            cloud['objects'][o]['width'] = width2
            cloud['objects'][o]['height'] = randint(25, 50)
            
        
        return cloud
        
    def update(self):
        
        for i in range(len(self.objects)):
        
            self.objects[i]['x'] += self.objects[i]['speed']
            if self.weatherOptions[self.shared[1]] == "storm":
                self.objects[i]['x'] += self.objects[i]['speed']
                
            if self.objects[i]['x']-self.objects[i]['width'] > 800:
                    
                if self.weatherOptions[self.shared[1]] != "clear":
                        
                    self.objects[i] = self.resetCloud(self.objects[i])
                          
            self.objects[i]['color'] = darken(self.colors[self.weatherOptions[self.shared[1]]], self.shared[0])
            
            for o in range(len(self.objects[i]['objects'])):
                
                object = self.objects[i]['objects'][o]
                
                self.queue.put(QueueItem("itemconfig", object['object'], fill = self.objects[i]['color'], outline = self.objects[i]['color']))
                self.queue.put(QueueItem("coords", object['object'], self.objects[i]['x']+object['x']-object['width'], self.objects[i]['y']+object['y']-object['height'], self.objects[i]['x']+object['x']+object['width'], self.objects[i]['y']+object['y']+object['height']))
        
        self.oldWeather = self.weatherOptions[self.shared[1]]
        
    def run(self):
        
        while self.paused[1] == 1:
            pass
        
        self.colors = {'clear': "#FFFFFF", 'cloudy': "#FFFFFF", 'overcast': "#969696", 'rain': "#646464", 'storm': "#323232"}
        self.oldWeather = "clear"
        
        self.objects = []
        for i in range(15):
            x = randint(1600, 2400)
            y = randint(0, 25)
            width = randint(175, 250)
            self.objects.append({
                                 'x': x,
                                 'y': y,
                                 'width': width,
                                 'speed': randint(5, 8),
                                 'color': "#FFFFFF",
                                 'objects': []})
            for o in range(3):
                width2 = randint(100, 175)
                x = randint(-width+width2, width-width2)
                y = randint(-5, 20)
                queueItem = QueueItem("create", 'oval', x, y, x, y, fill = "#FFFFFF", outline = "#FFFFFF")
                self.queue.put(queueItem)
                object = None
                while object == None:
                    object = queueItem.pipeRecv.recv()
                self.objects[i]['objects'].append({
                                                   'x': x,
                                                   'y': y,
                                                   'width': width2,
                                                   'height': randint(25, 50),
                                                   'object': object})
        
        self.queue.put(QueueItem("cont"))   
        self.paused[1] = 1
        while self.paused[1] == 1:
                pass
        
        while True:
            self.update()
            self.queue.put(QueueItem("cont"))
            self.paused[1] = 1
            sleep(0.05)
            while self.paused[1] == 1:
                pass
