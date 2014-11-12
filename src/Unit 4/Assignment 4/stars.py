'''
Created on Nov 11, 2014

@author: Jacob
'''
from multiprocessing import *
from utilities import *
from random import randint
from tkinter.constants import HIDDEN, NORMAL
from time import sleep

class Stars(Process):


    def __init__(self, queue, shared, paused):
        
        Process.__init__(self)
        self.daemon = True
        
        self.queue = queue
        self.shared = shared
        self.paused = paused
        
    def update(self):
        
        if self.shared[0] in range(850, 950):
            i = (self.shared[0]-850) * 2
            self.queue.put(QueueItem("itemconfig", self.stars[i]['object'], state = NORMAL))
            i += 1
            self.queue.put(QueueItem("itemconfig", self.stars[i]['object'], state = HIDDEN))
        elif self.shared[0] in range(1450, 1550):
            i = (self.shared[0]-1450) * 2
            self.queue.put(QueueItem("itemconfig", self.stars[i]['object'], state = HIDDEN))
            i += 1
            self.queue.put(QueueItem("itemconfig", self.stars[i]['object'], state = HIDDEN))
        
    def run(self):
        
        self.paused[0] = 1
        
        self.stars = []
        for i in range(200):
            
            self.stars.append({})
            self.stars[i]['x'] = randint(0, 800)
            self.stars[i]['y'] = randint(0, 400)
            self.stars[i]['size'] = randint(1, 3)
            queueItem = QueueItem("create", 'oval', self.stars[i]['x']-self.stars[i]['size'], self.stars[i]['y']-self.stars[i]['size'], self.stars[i]['x']+self.stars[i]['size'], self.stars[i]['y']+self.stars[i]['size'], fill = "white", outline = "white", state = HIDDEN)
            self.queue.put(queueItem)
            self.stars[i]['object'] = None
            while self.stars[i]['object'] == None:
                self.stars[i]['object'] = queueItem.pipeRecv.recv()
        
        while True:
            self.update()
            self.queue.put(QueueItem("cont"))
            self.paused[2] = 1
            sleep(0.05)
            while self.paused[2] == 1:
                pass