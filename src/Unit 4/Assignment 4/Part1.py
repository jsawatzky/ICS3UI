'''
Created on Oct 24, 2014

@author: Jacob Sawatzky
'''

from tkinter import *
from utilities import *

def getNames(tk):
    
    names = []
    
    label = Label(tk, text = "Please enter name #1:")
    entry = Entry(tk)
    tk.bind("<Return>", lambda event: names.append(entry.get()))
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
    clearScreen(tk)
    return names

def play(names, tk):
    
    rhyme = ["Eenie", "meenie", "miney", "moe", "catch", "a", "tiger", "by", "the", "toe"]
    
    nameLength = len(names)
    
    nameLabels = []
    for i in range(0, round((nameLength/5)+0.5)):
        for x in range(0, min((i+1)*5, nameLength-(i*5))):
            nameLabels.append(Label(tk, text = names[i*5+x]))
            nameLabels[len(nameLabels)-1].grid(row = i+1, column = x)
    
    while True:
        tk.update()
    
    while nameLength > 1:
        for i in range(0, len(rhyme)):
            pass

def run(tk):
    
    names = getNames(tk)
    play(names, tk)
    
    clearScreen(tk)

#Runs the program if not from menu
if __name__ == "__main__":
    run(Tk())