#######################################################################
# Title: Ye Olde Castle                                               #
# Programmer: Qianshu Wang                                            #
# Last Modified: December 12 2011                                     #
# Description: A scene of a castle at night made using python         #
#              graphics tools.                                        #
#######################################################################



# Imports graphics and random tools to be used in program.
from tkinter import *
from random import*


# Creates canvas for picture to be drawn on.
myInterface = Tk()
me = Canvas(myInterface, width=1000, height=1000, background="black")
me.pack ()


# Creates sky and ground.
me.create_rectangle (0, 700, 1000, 1000, fill = "ForestGreen")
me.create_rectangle (0,780, 1000, 850, fill = "sienna")


# Randomly generates stars for night sky.
for stars in range (0,1500):
    x1 = randint(0,1000)
    y1 = randint(0,697)
    starWidth = randint(1,4)
    me.create_oval (x1,y1, x1 + starWidth,y1 + starWidth, fill = "white", outline = "white")


# Generates crescent moon.    
me.create_oval (100,100, 300,300, fill = "yellow")
me.create_oval (180,100, 300,300, fill = "black")


# Generates shooting star.
me.create_line (900,150, 700,350, fill = "orange", width = 10, smooth = "true")
me.create_oval (680,330, 720,370, fill = "blue", outline = "blue") 


# Creates fruit tree and randomly generates fruits on it.
me.create_rectangle (150,750, 180,600, fill = "brown",)
me.create_polygon (80,450, 250,450, 250,620, 80,620,fill = "green", smooth = "true")
for fruit in range (0, 18):
    x2 = randint (100,230)
    y2 = randint (470, 600)
    fruitWidth = randint(12,16)
    me.create_oval (x2,y2, x2 + fruitWidth,y2 + fruitWidth, fill = "red", outline = "red")


# Creates birds in background.
me.create_line (110,180, 125,190, 140,210, 145,190,  160,180, fill = "black", width = 4, smooth = "false")
me.create_line (120,210, 135,220, 150,240, 165,220, 180,210, fill = "black", width = 4, smooth = "false")


# Generates castle in foreground and features of it.
me.create_rectangle (700,800, 900, 550, fill = "DimGray")
me.create_rectangle (650,550, 950, 585, fill = "DimGray", outline = "DimGray")
x3 = 650
y3 = 550
x4 = 680
y4 = 500
for CastleCrenellations in range (0,6):
    me.create_rectangle(x3,y3, x4,y4, fill = "DimGray", outline = "DimGray")
    x3 = x3 + 54
    x4 = x4 + 54
me.create_rectangle (700,800, 750,650, fill = "SaddleBrown")


# Creates text that is placed on the castle.
me.create_text (800,625, text = "Ye Olde Castle", font = "Times 20 italic bold", fill = "GoldenRod")


# Draws images on canvas.
me.update()





# END OF PROGRAM
