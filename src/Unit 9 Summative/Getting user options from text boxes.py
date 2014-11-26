from tkinter import *

ball = 0

def printName():
    global ball
    screen2.delete(ball)
    r = int(  radiusEntry.get() )
    ball = screen.create_oval(100, 100, 100+r, 100+r, fill="yellow")
    
root1 = Tk()
root1.title("Options")

root2 = Tk()
root2.title("View screen")
screen = Canvas(root2, height=200, width=200, background="blue")
screen.pack()

L = Label( root1, text="Radius: ")
L.pack( side = LEFT)

radiusEntry = Entry(root1)
radiusEntry.pack( side = LEFT)

b = Button(root1, text="Print name", command=printName)
b.pack( side = LEFT)

root1.mainloop()


