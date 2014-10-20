'''
Created on Oct 14, 2014

@author: Jacob Sawatzky
'''

from tkinter import *

WIDTH = 400
HEIGHT = 800

regionX = 0
regionY = 0

tk = Tk()
s = None
label = Label(tk, text = "How many rows of fractions do you want?")
entry = Entry(tk)
numRows = 0
def setNumRows():
    global WIDTH, HEIGHT, regionX, regionY, tk, label, entry, button, errorLabel, numRows
    try:
        numRows = int(entry.get())
        if numRows == 0:
            raise ValueError
    except ValueError:
        errorLabel = Label(tk, text = "You must enter an integer!")
        errorLabel.grid(row = 2, columnspan = 2)
    else:
        if numRows > WIDTH/25:
            regionX = numRows*25
        else:
            regionX = WIDTH
        ##ADD SCROLL BAR
        if numRows > HEIGHT/50:
            regionY = numRows*50
        else:
            regionY = HEIGHT
        label.destroy()
        entry.destroy()
        button.destroy()
        if errorLabel != None:
            errorLabel.destroy()
button = Button(tk, text = "Enter", command = setNumRows)
errorLabel = None

def drawBoxes():
    global s, regionX, regionY, numRows
    
    colors = ["red", "pink", "purple", "blue", "green", "yellow", "orange"]
    
    tileHeight = regionY/numRows
    
    for row in range(0, numRows):
        
        x1 = 0
        y1 = row*tileHeight
        
        tileWidth = regionX/(row+1)
        
        for column in range(0, row+1):
            
            x2 = x1 + tileWidth
            y2 = y1 + tileHeight
            
            s.create_rectangle(x1, y1, x2, y2, fill = colors[row%7])
            s.create_text(x1+((x2-x1)/2), y1+((y2-y1)/2), text = "_", fill = "black", font = "Times 10 bold", anchor = S)
            s.create_text(x1+((x2-x1)/2), y1+((y2-y1)/2)-5, text = "1", fill = "black", font = "Times 10 bold", anchor = S)
            s.create_text(x1+((x2-x1)/2), y1+((y2-y1)/2)+5, text = str(row+1), fill = "black", font = "Times 10 bold", anchor = N)
            
            x1 += tileWidth
    
    
    
def run():
    global s, numRows, WIDTH, HEIGHT, regionX, regionY, label, entry, button
    
    label.grid(row = 0, columnspan = 2)
    entry.grid(row = 1, column = 0, sticky = E)
    button.grid(row = 1, column = 1, sticky = W)
    
    while numRows == 0:
        try:
            tk.update()
        except:
            return
    
    scrollX = Scrollbar(tk, orient = HORIZONTAL)
    scrollY = Scrollbar(tk)
    if regionX > WIDTH:
        scrollX.grid(row = 1, column = 0, sticky = E+W)
    if regionY > HEIGHT:
        scrollY.grid(row = 0, column=1, sticky = N+S)
    s = Canvas(tk, width=WIDTH, height=HEIGHT, bg = "black", xscrollcommand = scrollX.set, yscrollcommand = scrollY.set)
    s.grid(row = 0, column = 0)
    scrollX.config(command = s.xview)
    scrollY.config(command = s.yview)
    
    drawBoxes()
    
    s.config(scrollregion=s.bbox(ALL))
    
    while True:
        try:
            s.update()
        except:
            return
        
if __name__ == "__main__":
    run()