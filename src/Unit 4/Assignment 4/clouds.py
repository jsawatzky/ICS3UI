'''
Created on Nov 8, 2014

@author: Jacob
'''
from utilities import QueueItem
from threading import Thread
from random import randint

class Clouds(Thread):
    
    def __init__(self, queue, mainThread):
        
        Thread.__init__(self)
        self.daemon = True
        
        self.queue = queue
        self.mainThread = mainThread
        
        self.colors = {'cloudy': "white", 'overcast': "#323232", 'rain': "#646464", 'storm': "#969696"}
        self.oldWeather = "clear"
        self.weather = "clear"
        
        self.objects = []
        for i in range(10):
            x = randint(800, 1600)
            y = randint(850, 1700)
            width = randint(50, 150)
            self.objects.append({
                                 'x': x,
                                 'y': y,
                                 'width': width,
                                 'speed': randint(1, 4),
                                 'color': "white",
                                 'objects': []})
            for o in range(5):
                x = randint(10, width-10)
                y = randint(10, 30)
                queueItem = QueueItem("create", 'oval', x, y, x, y, fill = "white", outline = "white")
                self.queue.put(queueItem)
                object = None
                while object == None:
                    object = queueItem.getObject()
                self.objects[i]['objects'].append({
                                                   'x': x,
                                                   'y': y,
                                                   'width': randint(10, min(x, width-x)),
                                                   'height': randint(10, min(y, 40-y)),
                                                   'object': object})
        
    def setWeather(self, weather):
        
        self.oldWeather = self.weather
        self.weather = weather
        
    def update(self):
        
        for i in range(len(self.objects)):
            self.objects[i]['x'] += self.objects[i]['speed']
            
            if self.weather != "clear":
                
                self.objects[i]['color'] = self.colors[self.weather]
                
                
    
    def draw(self):
        
        pass
        
    def run(self):
        
        while True:
            self.update()
            self.draw()