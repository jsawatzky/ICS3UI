from tkinter import *
from time import *
from random import *
from math import *
from colorsys import * 


tk = Tk()
Width = 1000
Height = 1000
BackGround = "midnight blue"
screen = Canvas(tk, width = Width, height = Height, background = BackGround)
screen.pack()

Ground = 800
TowerL = 400
TowerR = 600
TowerTop = 200

    
screen.create_rectangle (0, Ground, Width, Height, fill = "#5C3317")

PebNum = 1000
for Rocks in range (1, PebNum + 1):
    xPeb = randint(0, Width)
    yPeb = randint(Ground + 1, Height)
    size = randint (5, 10)
    screen.create_oval (xPeb, yPeb, xPeb + size, yPeb + size, fill = "#3D352A", outline = "#3D352A")

#Sauron's tower

screen.create_rectangle (TowerL, TowerTop, TowerR, Ground, fill = "black")
screen.create_polygon (TowerL, TowerTop, TowerL + 50, TowerTop, TowerL, TowerTop - 100, fill = "black")
screen.create_polygon (TowerR, TowerTop, TowerR - 50, TowerTop, TowerR, TowerTop - 100, fill = "black")
screen.create_polygon (250, Ground, TowerL, 450, TowerL, Ground, fill = "black")
screen.create_polygon (TowerR, 450, TowerR, Ground, TowerR + 150, Ground, fill = "black")
screen.create_polygon(TowerR, 350, TowerR + 50, 300, TowerR + 50, 100, TowerR, 100, fill = "black")
screen.create_polygon(TowerL, 350, TowerL - 50, 300, TowerL - 50, 100, TowerL, 100, fill = "black")
screen.create_oval(150, 0, TowerL, 150, fill = "midnight blue", outline = "midnight blue")
screen.create_oval(TowerR, 0, 850, 150, fill = "midnight blue", outline = "midnight blue")
screen.create_oval(TowerR + 1, 190, 850, Ground - 50, fill = "midnight blue", outline = "midnight blue")
screen.create_oval(TowerL - 1, 190, 150, Ground - 50, fill = "midnight blue", outline = "midnight blue")


#the eye

EyeTop = 125
EyeBottom = 175

screen.create_oval(TowerL + 50, EyeTop, TowerR - 50, EyeBottom, fill = "gold", outline = "gold")
screen.create_oval(TowerL + 65, EyeTop + 2, TowerR - 65, EyeBottom - 2, fill = "orange red", outline = "orange red")
screen.create_oval(TowerL + 75, EyeTop + 2, TowerR - 75, EyeBottom - 2, fill = "red", outline = "red")
screen.create_oval(TowerL + 93, EyeTop + 4, TowerR - 93, EyeBottom- 4, fill = "black")

#Blood Moon

xMoon1 = 750
yMoon1 = 50
xMoon2 = xMoon1 + 150
yMoon2 = yMoon1 + 150
screen.create_oval( xMoon1, yMoon1, xMoon2, yMoon2, fill = "#323232", outline = "#602020" )      

#Rain

Fall = 500
for Rain in range (0, Fall + 1):
    xRain = randint(0 , Width)
    yRain = randint(0, Height)
    RainDrop = screen.create_line(xRain, yRain, xRain + 10, yRain + 10, fill = "dark red")

#text

screen.create_text(500, 900, fill = "dark red", font = "Times 40", text = "Sauron's Tower")


screen.create_line(325, 875, 675, 875, 675, 925, 325, 925, 325, 875, fill = "red", width = 3)

screen.update()


