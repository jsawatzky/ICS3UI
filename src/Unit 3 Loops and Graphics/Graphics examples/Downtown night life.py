#TITLE: TKINTER STILL PICTURE
#PROGRAMMER:  DANIEL ZHOU
#LAST MODIFIED: DECEMBER 21, 2011
#PURPOSE: DRAW A REALISTIC PICTURE USING TKINTER
#----------------------------------------------------------------------



from tkinter import *
from random import *
import time


tk = Tk()
tk = Canvas(tk, width=800,height=800,background="black")
tk.pack()


tk.create_rectangle(0, 400, 800, 800, fill = "gray")

color = 0
for star in range(0, 200):
    x = randint(0, 800)
    y = randint(0, 395)
    size = randint(1, 5)
    color = color + 1
    tk.create_oval(x, y, x + size, y + size, fill = "white", width = 0)
    if color == 6:
        tk.create_oval(x, y, x + size, y + size, fill = "yellow", width = 0)
    if color == 12:
        tk.create_oval(x, y, x + size, y + size, fill = "red", width = 0)
        color = 0

tk.create_oval(50, 50, 150, 150, fill = "grey")

tk.create_oval(120, 120, 135, 135, fill = "dark gray")
tk.create_oval(100, 90, 120, 110, fill = "dark gray")
tk.create_oval(90, 125, 105, 140, fill = "dark gray")
tk.create_oval(60, 100, 80, 120, fill = "dark gray")
tk.create_oval(100, 60, 115, 75, fill = "dark gray")

distance = 0
for distantbuilding in range(0, 10):
    y = randint(100, 300)
    tk.create_rectangle(distance, 500, distance + 100, y, fill = "dimgray")
    distance = distance + 100

tk.create_rectangle(0, 700, 300, 300, fill = "saddlebrown")
tk.create_rectangle(0, 700, 20, 300, fill = "slategray")
tk.create_rectangle(300, 700, 280, 300, fill = "slategray")
tk.create_polygon(75, 350, 55, 370, 95, 370, fill = "black")
x = 0
for lightray in range(0, 15):
    x = x + 10
    tk.create_line(75, 370, 0 + x, 470, fill = "yellow")




tk.create_polygon(225, 350, 205, 370, 245, 370, fill = "black")
x = 0
for lightray in range(0, 15):
    x = x + 10
    tk.create_line(225, 370, 150 + x, 470, fill = "yellow")

tk.create_rectangle(50, 500, 250, 550, fill = "brown")
tk.create_text(150, 525, text="BAR", font="times 30", fill = "midnightblue")
tk.create_rectangle(50, 600, 150, 650, fill = "azure")
tk.create_rectangle(200, 600, 250, 700, fill = "gray")
tk.create_oval(210, 650, 215, 655, fill = "black")
tk.create_polygon(350, 700, 320, 700, 320, 650, 335, 640, 350, 640, 350, 650, fil = "dark green", outline = "black", width = 2)
tk.create_rectangle(350, 700, 800, 200, fill = "darkgray")


x = 380
y = 670
increase = 1
for window in range(0, 25):
    tk.create_rectangle(x, y, x + 60, y - 60, fill = "azure")
    y = y - 90
    if y < 300:
        y = 670
        x = x + 90
    




tk.create_line(0, 450, 200, 550, 400, 450, smooth = "true")
tk.create_line(400, 450, 600, 550, 800, 450, smooth = "true")
tk.create_rectangle(0, 800, 10, 450, fill = "black")
tk.create_rectangle(10, 500, 30, 550, fill = "gainsboro")
tk.create_rectangle(400, 800, 410, 450, fill = "black")
tk.create_rectangle(410, 500, 430, 550, fill = "gainsboro")
tk.create_rectangle(790, 800, 800, 450, fill = "black")

tk.create_rectangle(160, 780, 170, 570, fill = "dimgray")
tk.create_rectangle(150, 570, 180, 580, fill = "dimgray")
x = 0
for lightray in range(0, 15):
    x = x + 10
    tk.create_line(165, 580, 85 + x, 670, fill = "yellow")

tk.create_rectangle(640, 780, 650, 570, fill = "dimgray")
tk.create_rectangle(630, 570, 660, 580, fill = "dimgray")
x = 0
for lightray in range(0, 15):
    x = x + 10
    tk.create_line(645, 580, 575 + x, 670, fill = "yellow")






for person in range(0, 3):
    x = randint(0, 800)
    tk.create_oval(x, 650, x + 40, 690, fill = "blue")
    tk.create_line(x + 20, 690, x + 20, 750, width = 2)
    tk.create_line(x + 20, 690, x + 5, 710, x + 5, 710, x + 4, 730, width = 2)

    
    tk.create_line(x + 20, 690, x + 30, 710, x + 30, 710, x + 50, 730, width = 2)


    tk.create_line(x + 20, 750, x + 15, 770, x - 10, 800, width = 2)
    tk.create_line(x + 20, 750, x + 25, 770, x + 35, 800, width = 2)







tk.create_line(0, 450, 200, 550, 400, 450, smooth = "true")
tk.create_line(400, 450, 600, 550, 800, 450, smooth = "true")
tk.create_rectangle(0, 800, 10, 450, fill = "black")
tk.create_rectangle(10, 500, 30, 550, fill = "gainsboro")
tk.create_rectangle(400, 800, 410, 450, fill = "black")
tk.create_rectangle(410, 500, 430, 550, fill = "gainsboro")
tk.create_rectangle(790, 800, 800, 450, fill = "black")


tk.create_text(100, 780, text="By Daniel Zhou", font="times 20", fill = "red")




tk.update()

