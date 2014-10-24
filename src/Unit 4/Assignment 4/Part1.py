'''
Created on Oct 24, 2014

@author: Jacob Sawatzky
'''

from tkinter import *

def getNames(tk):
    
    names = []
    
    label = Label(tk, text = "Please enter name #1:")
    entry = Entry(tk)
    enterButton = Button(tk, text = "Enter", command = lambda: names.append(entry.get()))
    doneButton = Button(tk, text = "Done", command = lambda: names.append("done"))
    label.grid(row = 0, column = 0, columnspan = 2)
    entry.grid(row = 1, column = 0)
    enterButton.grid(row = 1, column = 1)
    doneButton.grid(row = 2, column = 0, columnspan = 2)
    
    oldSize = 0
    
    while names.count("done") == 0:
        while len(names) == oldSize:
            tk.update()
        entry.delete(0, END)
        label.config(text = "Please enter name #" + str(len(names)+1) + ":")
        oldSize = len(names)
        
    names.remove("done")
    return names

def run():
    
    tk = Tk()
    
    names = getNames(tk)
    print(names)

if __name__ == "__main__":
    run()