'''
Created on Oct 27, 2014

@author: Jacob Sawatzky
'''
from tkinter import *
from utilities import *
import Part1#, Part2, Part3, Part4

#Edit for assignment
assignmentName = "Assignment __"
assignmentParts = [('Part1', Part1), ('Part2', Part2), ('Part3', Part3), ('Part4', Part4)]

cont = Boolean(False)
done = Boolean(False)

#Start the tk window
tk = Tk()
tk.focus_force()

#Create the menu widgets
widgets = {}
widgets['mainLabel1'] = Label(tk, text = "Welcome to", font = "Times 25 bold")
widgets['mainLabel2'] = Label(tk, text = assignmentName, font = "Times 25 bold")
widgets['instruction'] = Label(tk, text = "Please pick a part", font = "Times 15")
selected = Variable(tk)
widgets['partMenuOptions'] = []
for name, module in assignmentParts:
    widgets['partMenuOptions'].append(Radiobutton(tk, text = name, variable = selected, value = name))
widgets['selectButton'] = Button(tk, text = "Select", command = lambda: cont.set(True))
widgets['doneButton'] = Button(tk, text = "Done", command = lambda: done.set(True))
widgets['credits'] = Label(tk, text = "By: Jacob Sawatzky", font = "Times 10")

#Bind keyboard events
tk.bind("<Return>", lambda event: cont.set(True))
tk.bind("<Escape>", lambda event: done.set(True))

while done.get() == False:
    
    #Place the widgets on screen
    widgets['mainLabel1'].grid(row = 0, column = 0, columnspan = 2)
    widgets['mainLabel2'].grid(row = 1, column = 0, columnspan = 2)
    widgets['instruction'].grid(row = 2, column = 0, columnspan = 2)
    selected.set("Choose an option...")
    i = 3
    for option in widgets['partMenuOptions']:
        option.grid(row = i, column = 0)
        i += 1
    widgets['selectButton'].grid(row = 3, column = 1, rowspan = len(assignmentParts))
    widgets['doneButton'].grid(row = 4+len(assignmentParts), column = 0, sticky = W)
    widgets['credits'].grid(row = 4+len(assignmentParts), column = 1, sticky = E)
    
    #Wait for the user to pick an option
    while cont.get() == False and done.get() == False:
        try:
            tk.update()
        except:
            done.set(True)
            
    #Kill program if user quits
    if done.get() == True:
        try:
            tk.destroy()
        except:
            pass
        break
    
    #Reset continue var
    cont.set(False)
    
    #Take widgets off screen
    clearScreen(tk)
    
    #Run the correct program
    for name, module in assignmentParts:
        if selected.get() == name:
            module.run(tk)