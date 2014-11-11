'''
Created on Nov 8, 2014

@author: Jacob
'''
from utilities import *

class Sun():
    
    def __init__(self, queue, startY, peak):
        self.queue = queue
        self.k = peak
        self.h = 400
        self.a = (startY - self.k)/(self.h**2)
        print(1)
        queueItem = QueueItem("create", 'oval', -75, startY-75, 75, startY+75, fill = "yellow", outline = "yellow")
        self.queue.put(queueItem)
        
        self.object = None
        while self.object == None:
            self.object = queueItem.pipeRecv.recv()
            
    def update(self, time):
        if time > 1525:
            time -= 1600
        self.x = time
        self.y = self.a*((time-self.h)**2) + self.k
        
    def draw(self):
        
        self.queue.put(QueueItem("coords", self.object, self.x-75, self.y-75, self.x+75, self.y+75))