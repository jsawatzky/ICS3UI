'''
Created on Nov 8, 2014

@author: Jacob
'''
from utilities import *

class Sky():
    
    def __init__(self, queue):
        self.queue = queue
        colors = {}
        colors['sunrise'] = "#FFC012"
        colors['sunset'] = "#DE8501"
        colors['day'] = "#3AA0FF"
        colors['night'] = "#121C43"
        self.colors = colors
        
        
    def update(self, time):
        
        colors = self.colors
        
        if time in range(0, 26):
            color = getColor(getColor(colors['sunset'], colors['sunrise'], 0, 2, 1), colors['sunrise'], 0, 25, time)
        elif time in range(26, 76):
            color = getColor(colors['sunrise'], colors['day'], 26, 75, time)
        elif time in range(76, 726):
            color = "#3AA0FF"
        elif time in range(726, 776):
            color = getColor(colors['day'], colors['sunrise'], 726, 775, time)
        elif time in range(776, 826):
            color = getColor(colors['sunrise'], colors['sunset'], 776, 825, time)
        elif time in range(826, 876):
            color = getColor(colors['sunset'], colors['night'], 826, 875, time)
        elif time in range(876, 1526):
            color = "#121C43"
        elif time in range(1526, 1576):
            color = getColor(colors['night'], colors['sunset'], 1526, 1576, time)
        elif time in range(1576, 1601):
            color = getColor(colors['sunset'], getColor(colors['sunset'], colors['sunrise'], 0, 2, 1), 1576, 1600, time)
            
        self.queue.put(QueueItem("config", background = color))