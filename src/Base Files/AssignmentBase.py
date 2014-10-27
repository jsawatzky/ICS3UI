from tkinter import *
from utilities import *
import Part1, Part2, Part3, Part4

assignmentName = "Assignment __"
assignmentParts = {'Part1': Part1, 'Part2': Part2, 'Part3': Part3, 'Part4': Part4}
cont = Boolean(False)
done = Boolean(False)

tk = Tk()

widgets = {}

widgets['mainLabel1'] = Label(tk, text = "Welcome to", font = "Times 25 bold")
widgets['mainLabel2'] = Label(tk, text = assignmentName, font = "Times 25 bold")
widgets['instruction'] = Label(tk, text = "Please pick a part", font = "Times 15")
selected = StringVar(tk)
widgets['partMenu'] = OptionMenu(tk, selected, assignmentParts.keys())
widgets['selectButton'] = Button(tk, text = "Select", command = lambda: cont.set(True))
widgets['doneButton'] = Button(tk, text = "Done", command = lambda: done.set(True))
widgets['credits'] = Label(tk, text = "By: Jacob Sawatzky", font = "Times 10")

tk.bind("<Return>", lambda event: cont.set(True))
tk.bind("<Escape>", lambda event: done.set(True))

while done.get() == False:
    
    widgets['mainLabel1'].grid(row = 0, column = 0, columnspan = 2)
    widgets['mainLabel2'].grid(row = 1, column = 0, columnspan = 2)
    widgets['instruction'].grid(row = 2, column = 0, columnspan = 2)
    selected.set("Choose an option...")
    widgets['partMenu'].grid(row = 3, column = 0)
    widgets['selectButton'].grid(row = 3, column = 1)
    widgets['doneButton'].grid(row = 4, column = 0, sticky = W)
    widgets['credits'].grid(row = 4, column = 1, sticky = E)
    
    while cont.get() == False and done.get() == False:
        try:
            tk.update()
        except:
            done.set(True)
            
    if done.get() == True:
        try:
            tk.destroy()
        except:
            pass
        break
    
    for widget in widgets:
        widget.grid_forget()
        
    for part in assignmentParts.keys():
        if selected.get() == part:
            assignmentParts[part].run(tk)