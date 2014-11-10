'''
Created on Nov 8, 2014

@author: Jacob
'''
from utilities import *

class Moon():
    
    def __init__(self, queue, startY, peak):
        self.queue = queue
        self.k = peak
        self.h = 400
        self.a = (startY - self.k)/(self.h**2)
        
        queueItemBack1 = QueueItem("create", 'arc', 0, 0, 0, 0, fill = "#0e1637", outline = "#0e1637", start = 270, extent = 180)
        queueItemBack2 = QueueItem("create", 'arc', 0, 0, 0, 0, fill = "#0e1637", outline = "#0e1637", start = 90, extent = 180)
        queueItemFront = QueueItem("create", 'oval', 0, 0, 0, 0, fill = "white", outline = "white")
        
        self.queue.put(queueItemBack1)
        self.queue.put(queueItemBack2)
        self.queue.put(queueItemFront)
        
        self.back1 = None
        self.back2 = None
        self.front = None
        while self.back1 == None or self.back2 == None or self.front == None:
            self.back1 = queueItemBack1.getObject()
            self.back2 = queueItemBack2.getObject()
            self.front = queueItemFront.getObject()
        
    def update(self, time, day):
        if time < 100:
            day -= 1
        time -= 800
        if time < -50:
            time += 1600
        self.x = time
        self.y = self.a*((time-self.h)**2) + self.k
        
        day %= 8
        
        if day < 2 or day > 5:
            self.queue.put(QueueItem("itemconfig", self.front, fill = "white", outline = "white"))
        else:
            self.queue.put(QueueItem("itemconfig", self.front, fill = "#0e1637", outline = "#0e1637"))
            
        if day == 0:
            self.queue.put(QueueItem("itemconfig", self.back1, fill = "white", outline = "white"))
            self.queue.put(QueueItem("itemconfig", self.back2, fill = "white", outline = "white"))
        elif 0 < day < 4:
            self.queue.put(QueueItem("itemconfig", self.back1, fill = "white", outline = "white"))
            self.queue.put(QueueItem("itemconfig", self.back2, fill = "#0e1637", outline = "#0e1637"))
        elif day == 4:
            self.queue.put(QueueItem("itemconfig", self.back1, fill = "#0e1637", outline = "#0e1637"))
            self.queue.put(QueueItem("itemconfig", self.back2, fill = "#0e1637", outline = "#0e1637"))
        else:
            self.queue.put(QueueItem("itemconfig", self.back1, fill = "#0e1637", outline = "#0e1637"))
            self.queue.put(QueueItem("itemconfig", self.back2, fill = "white", outline = "white"))
            
        day %= 4
        
        if day == 0:
            self.size = 50
        elif day == 2:
            self.size = 0
        elif day == 1 or day == 3:
            self.size = 25
        
    def draw(self):
        
        self.queue.put(QueueItem("coords", self.back1, self.x-50, self.y-50, self.x+50, self.y+50))
        self.queue.put(QueueItem("coords", self.back2, self.x-50, self.y-50, self.x+50, self.y+50))
        self.queue.put(QueueItem("coords", self.front, self.x-self.size, self.y-50, self.x+self.size, self.y+50))