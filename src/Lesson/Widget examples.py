from tkinter import *

root = Tk()

#The Label widget

label = Label(root, text = "Hello World")
label.grid(row = 0, column = 0)

###The button widget
##
##def sayHi():
##    print("Hi!")
##
##button = Button(root, text = "Hi!", command = sayHi)
##button.grid(row = 1, column = 0)
##
###The Entry widget
##
##entry = Entry(root)
##entry.grid(row = 2, column = 0)
##
###entry.insert(0, "Default")
##
###entry.delete(0, END)
##
##def getEntry():
##    value = entry.get()
##
##    print(value)
##
##entryButton = Button(root, text = "Get", command = getEntry)
##entryButton.grid(row = 2, column = 1)
