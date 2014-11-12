'''
Created on Nov 8, 2014

@author: Jacob
'''
from utilities import *

class Ground():
    
    def __init__(self, queue):
        
        self.queue = queue
        
        colors = {}
        
        colors['spring'] = "#01A611"
        colors['summer'] = "#005C09"
        colors['fall'] = "#007B0C"
        colors['winter'] ="#FFFFFF"
        
        self.colors = colors
        queueItem = QueueItem("create", 'rectangle', 0, 400, 800, 800, fill = colors['spring'], outline = colors['spring'])
        self.queue.put(queueItem)
        
        self.object = None
        while self.object == None:
            self.object = queueItem.pipeRecv.recv()
        
    def update(self, time, season, seasonStage, seasons):
        
        if seasonStage == "late":
            self.color = getColor(self.colors[season], getColor(self.colors[season], self.colors[seasons[(seasons.index(season)+1)%4]], 0, 2, 1), 0, 1600, time)
        elif seasonStage == "early":
            self.color = getColor(getColor(self.colors[season], self.colors[seasons[(seasons.index(season)+1)%4]], 0, 2, 1), self.colors[season], 0, 1600, time)
        else:
            self.color = self.colors[season]
            
        self.color = darken(self.color, time)
            
    def draw(self):
            
        self.queue.put(QueueItem("itemconfig", self.object, fill = self.color, outline = self.color))