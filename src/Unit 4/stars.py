'''
Created on Nov 11, 2014

@author: Jacob
'''
from multiprocessing import *
from utilities import *

class Stars(Process):


    def __init__(self, queue, shared, paused):
        
        Process.__init__(self)
        self.daemon = True
        
        self.queue = queue
        self.shared = shared
        self.paused = paused
        
    def update(self):
        
        pass
        
    def run(self):
        
        while True:
            self.update()
            self.queue.put(QueueItem("cont"))
            self.paused[2] = 1
            sleep(0.05)
            while self.paused[2] == 1:
                pass