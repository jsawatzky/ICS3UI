'''
Created on Nov 8, 2014

@author: Jacob
'''
from utilities import QueueItem
from threading import Thread
from random import randint

class Clouds(Thread):
    
    def __init__(self, queue):
        
        Thread.__init__(self)
        
        self.queue = queue
        
        self.colors = {'cloudy': "white", 'overcast': "#323232", 'rain': "#646464", 'storm': "#969696"}
        self.oldWeather = "clear"
        self.weather = "clear"
        
        self.objects = []
        for i in range(10):
            width = randint(50, 150)
            self.objects.append({
                                 'width': width,
                                 'speed': randint(1, 4),
                                 'objects': []})
            for x in range(5):
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
        
        pass
    
    def draw(self):
        
        pass
        
    def run(self):
        
        while True:
            self.update()
            self.draw()