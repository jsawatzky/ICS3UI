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
        self.daemon = True
        
        self.queue = queue
        
        self.shared = shared
        self.paused = paused
        
        self.weatherOptions =  ["clear", "clear", "clear", "clear", "cloudy", "cloudy", "overcast", "rain", "rain", "storm"]
        
    def resetCloud(self, cloud):
        
        width = randint(50, 150)
        cloud['x'] = cloud['x']%800 - 800
        cloud['y'] = randint(50, 100)
        cloud['width'] = width
        cloud['speed'] = randint(1, 4)
        
        return cloud
        
    def update(self):
        
        for i in range(len(self.objects)):
        
            self.objects[i]['x'] += self.objects[i]['speed']
                
            if self.objects[i]['x']-self.objects[i]['width']/2 > 800:
                    
                if self.weatherOptions[self.shared[1]] != "clear":
                        
                    self.objects[i] = self.resetCloud(self.objects[i])
                          
            self.objects[i]['color'] = darken(self.colors[self.weatherOptions[self.shared[1]]], self.shared[0])
            
            for o in range(len(self.objects[i]['objects'])):
                
                object = self.objects[i]['objects'][o]
                
                self.queue.put(QueueItem("itemconfig", object['object'], fill = self.objects[i]['color'], outline = self.objects[i]['color']))
                self.queue.put(QueueItem("coords", object['object'], self.objects[i]['x']+object['x']-object['width'], self.objects[i]['y']+object['y']-object['height'], self.objects[i]['x']+object['x']+object['width'], self.objects[i]['y']+object['y']+object['height']))
        
    def run(self):
        
        self.colors = {'clear': "#FFFFFF", 'cloudy': "#FFFFFF", 'overcast': "#969696", 'rain': "#646464", 'storm': "#323232"}
        
        self.objects = []
        for i in range(10):
            x = randint(900, 1500)
            y = randint(0, 25)
            width = randint(100, 200)
            self.objects.append({
                                 'x': x,
                                 'y': y,
                                 'width': width,
                                 'speed': randint(1, 4),
                                 'color': "#FFFFFF",
                                 'objects': []})
            for o in range(3):
                x = randint(int(-width/2)+10, int(width/2)-10)
                y = randint(-25, 0)
                queueItem = QueueItem("create", 'oval', x, y, x, y, fill = "#FFFFFF", outline = "#FFFFFF")
                self.queue.put(queueItem)
                object = None
                while object == None:
                    object = queueItem.pipeRecv.recv()
                self.objects[i]['objects'].append({
                                                   'x': x,
                                                   'y': y,
                                                   'width': randint(75, 125),
                                                   'height': randint(25, 50),
                                                   'object': object})
        
        while True:
            self.update()
            self.queue.put(QueueItem("cont"))
            self.paused[1] = 1
            sleep(0.05)
            while self.paused[1] == 1:
                pass
