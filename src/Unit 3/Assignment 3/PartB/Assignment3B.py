'''
Created on Oct 21, 2014

@author: Jacob Sawatzky
'''

import Part1, Part2, Part3, Part4
from tkinter import *

done = False
def doneF():
    global done
    done = True

continueB = False
def Continue():
    global continueB
    continueB = True

while done == False:
    
    tk = Tk()
    
    label = Label(tk, text = "Welcome to", font = "Times 25 bold")
    label2 = Label(tk, text = "Assignment 3B", font = "Times 25 bold")
    label3 = Label(tk, text = "Please pick a part", font = "Times 15")
    selected = StringVar(tk)
    menu = OptionMenu(tk, selected, "Checker Board", "Fraction Wall", "Single Ripple", "Multi Ripple")
    button = Button(tk, text = "Enter", command = Continue)
    button2 = Button(tk, text = "Done", command = doneF)
    label4 = Label(tk, text = "By: Jacob Sawatzky", font = "Times 10")
    
    label.grid(row = 0, column = 0, columnspan = 2)
    label2.grid(row = 1, column = 0, columnspan = 2)
    label3.grid(row = 2, column = 0, columnspan = 2)
    selected.set("Choose an option...")
    menu.grid(row = 3, column = 0)
    button.grid(row = 3, column = 1)
    button2.grid(row = 4, column = 0, sticky = W)
    label4.grid(row = 4, column = 1, sticky = E)
    
    while continueB == False and done == False:
        try:
            tk.update()
        except:
            done = True
            break
        
    if done == True:
        tk.destroy()
        break
    continueB = False
    selectedO = selected.get()
    tk.destroy()
    
    if selectedO == "Checker Board":
        Part1.run()
    elif selectedO == "Fraction Wall":
        Part2.run()
    elif selectedO == "Single Ripple":
        Part3.run()
    elif selectedO == "Multi Ripple":
        Part4.run()
    
