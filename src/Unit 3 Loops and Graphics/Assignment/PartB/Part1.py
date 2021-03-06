'''
Created on Oct 14, 2014

@author: Jacob Sawatzky
'''

from tkinter import *

done = False

s = None
label = None
button = None

WIDTH = 800
HEIGHT = WIDTH

tileSize = WIDTH/8

def doneF():
    global done
    done = True

def draw(s):
    for row in range(0, 8):
        
        if row % 2 == 0:
            x1 = 0
        else:
            x1 = tileSize
        y1 = row*tileSize
        y2 = y1 + tileSize
        
        for column in range(0, 8, 2):
            
            x2 = x1 + tileSize
            
            s.create_rectangle(x1, y1, x2, y2, fill = "red", outline="red")
            
            if row < 3:
                color = "blue"
            elif row > 4:
                color = "green"
            else:
                color = None
                
            if color != None:
                s.create_oval(x1+10, y1+10, x2-10, y2-10, fill = color, outline = "black")
            
            x1 += tileSize*2
        
def run():
    global done, s, label, doneB
    
    tk = Tk()
    tk.focus_force()
    
    label = Label(tk, text = "Checker Board", font = "Times 20 bold")
    label.grid(row = 0, sticky = W)
    doneB = Button(tk, text = "Done", command = doneF, width = 10)
    doneB.grid(row = 0, column = 1, sticky = E)
    s = Canvas(tk, width=WIDTH, height=HEIGHT, bg = "black")
    s.grid(row = 1, column = 0, columnspan = 2)
    draw(s)
    while done == False:
        try:
            s.update()
        except:
            break
    try:
        tk.destroy()
    except:
        pass
        
if __name__ == "__main__":
    run()