'''
Created on Oct 14, 2014

@author: Jacob Sawatzky
'''

from tkinter import *

done = False

def doneF():
    global done
    done = True

WIDTH = 400
HEIGHT = 800

regionX = 0
regionY = 0

s = None
label = None
entry = None
button = None
errorLabel = None
scrollX = None
scrollY = None
doneB = None
label2 = None
numRows = 0
def setNumRows(self = None):
    global WIDTH, HEIGHT, regionX, regionY, tk, label, entry, button, errorLabel, numRows
    try:
        numRows = int(entry.get())
        if numRows <= 0:
            raise ValueError
    except ValueError:
        entry.delete(0, END)
        return
    else:
        entry.delete(0, END)
        if numRows > WIDTH/25:
            regionX = numRows*25
        else:
            regionX = WIDTH
        if numRows > HEIGHT/50:
            regionY = numRows*50
        else:
            regionY = HEIGHT
        if errorLabel != None:
            errorLabel.destroy()
        drawBoxes()

def drawBoxes():
    global s, regionX, regionY, numRows
    
    s.delete(ALL)
    
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
            
    
    s.config(scrollregion=s.bbox(ALL))
    
def run():
    global s, numRows, WIDTH, HEIGHT, regionX, regionY, label, entry, button, done, scrollX, scrollY, label2, doneB
    
    tk = Tk()
    tk.focus_force()
    
    label2 = Label(tk, text = "Fraction Wall", font = "Times 20 bold")
    label2.grid(row = 0, sticky = W)
    doneB = Button(tk, text = "Done", command = doneF, width = 10)
    doneB.grid(row = 0, column = 1, columnspan = 2, sticky = E)
    
    label = Label(tk, text = "How many rows of fractions do you want:")
    label.grid(row = 1, sticky = W)
    entry = Entry(tk)
    entry.bind("<Return>", setNumRows)
    entry.grid(row = 1, column = 1, sticky = E)
    button = Button(tk, text = "Enter", command = setNumRows)
    button.grid(row = 1, column = 2, sticky = W)
    
    scrollX = Scrollbar(tk, orient = HORIZONTAL)
    scrollY = Scrollbar(tk)
    scrollX.grid(row = 4, column = 0, sticky = E+W, columnspan = 3)
    scrollY.grid(row = 3, column=3, sticky = N+S)
    s = Canvas(tk, width=WIDTH, height=HEIGHT, bg = "black", xscrollcommand = scrollX.set, yscrollcommand = scrollY.set)
    s.grid(row = 3, column = 0, columnspan = 3)
    scrollX.config(command = s.xview)
    scrollY.config(command = s.yview)
    
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