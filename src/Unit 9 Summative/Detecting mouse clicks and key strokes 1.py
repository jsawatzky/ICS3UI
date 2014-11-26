from tkinter import *
root = Tk()
screen = Canvas(root, width=200, height=200)


def mouseClickDetector(event):
    print ( "Mouse was clicked at " + str( event.x ) + "," + str(event.y ))


def keyPressDetector(event):
    print ("You just pressed the " + event.keysym + " key")



screen.bind( "<Key>",  keyPressDetector )
screen.bind("<Button-1>", mouseClickDetector)
screen.focus_set()
screen.pack()

root.mainloop()
