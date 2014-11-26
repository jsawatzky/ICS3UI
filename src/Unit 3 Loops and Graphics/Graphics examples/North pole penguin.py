#TITLE: North Pole Scene ft. Mr. Penguin
#PROGRAMMER: Madeleine Lee
#LAST MODIFIED: DECEMBER 17, 2013
#----------------------------------------------------------------------

from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=1500, height=1500, background="sky blue")
screen.pack()


#Ground 
screen.create_rectangle(0, 670, 1500, 1500, fill = "white")

#SnowFall
for snow in range (0, 400):
    x = randint(0, 1500)
    y = randint(0, 625)
    snow = randint(1, 5)
    screen.create_oval(x, y, x+snow, y+snow, fill = "white", width = 0)

###NORTHPOLE
#Pole
screen.create_rectangle(100, 300, 150, 670, fill = "white")

#Light
screen.create_oval(90, 240, 160, 310, fill = "Yellow")

#Stripes
numStripes = 13
gap = 30
y = 280

for pole in range (1, numStripes):
    stripeColour=choice(["Dark Violet", "Red", "Deep Pink", "Cyan"])
    y = y + gap
    screen.create_polygon(100, y, 150, y+20, 150, y+28, 100, y+8, fill = "Firebrick")


#Sign
screen.create_rectangle(50, 320, 200, 360, fill = "Peru")
screen.create_text(125,340, fill="White", font="Times 20 bold", text="North Pole",)

####Flag
##screen.create_polygon(150, 315, 150, 340, 250, 350, 275, 325, 250, 310, 150, 315, fill="white")
###Flag Text

##
###Santas House
#Roof
screen.create_oval(250, 200, 700, 575, fill = "Firebrick")

#Building
screen.create_rectangle(250, 350, 700, 670, fill = "Peru")

###Sign
screen.create_rectangle(265, 360, 395, 400, fill="Firebrick")
screen.create_text(325, 380, fill="white", font="Times 28 bold", text="Claus'")

#Window
screen.create_oval(500, 360, 650, 510, fill = "white")
screen.create_oval(510, 370, 640, 500, fill = "Yellow")
screen.create_line(575, 370, 575, 500, fill = "white", width = 8)
screen.create_line(510, 435, 640, 435, fill = "white", width = 8)

#Door
screen.create_rectangle(290, 515, 460, 670, fill = "brown", outline="brown")
screen.create_oval(289, 440, 462, 564, fill = "brown", outline="brown")
screen.create_rectangle(300, 515, 450, 670, fill = "Tan", outline="Tan")
screen.create_oval(300, 450, 450, 560, fill = "Tan", outline="Tan")

#Door knob
screen.create_oval(420, 560, 440, 580, fill="brown")


#Chimney Smoke

#First Cloud
screen.create_oval(300, 150, 350, 200, fill = "grey", outline= "grey")

#Random Clouds
for smoke in range (1, 10):
    x1 = randint(200, 400)
    y1 = randint(0, 180)
    x2 = randint(200, 400)
    y2 = randint(0, 180)
    screen.create_oval(x1, y1, x2, y2, fill="grey", outline = "grey")
    
###Chimney
screen.create_polygon(300, 300, 350, 300, 350, 200, 300, 200, 300, 300, fill = "white",)

#Chimney Stripes
numStripes = 4
gap = 30
y = 180

for pole in range (1, numStripes):
    y = y + gap
    screen.create_polygon(300, y, 350, y+20, 350, y+28, 300, y+8, fill = "Yellow")

##Christmas Tree

#Trunk
screen.create_rectangle(800, 600, 900, 670, fill = "Saddle Brown")

#Tree
screen.create_polygon(725, 600, 975, 600, 940, 530, 975, 530, 940, 460, 975, 460, 940, 390, 975, 390, 850, 300, 725, 390, 760, 390, 725, 460, 760, 460, 725, 530, 760, 530, 725, 600, 725, 600, fill = "Dark Green")

#Random Ornaments
for tree in range (1, 20):
    ornaments = choice(["Dark Violet", "Red", "Deep Pink", "Cyan", "Lawn Green", "Pink", "Deep Pink", "Orange", "Aquamarine", "White"])
    x1 = randint(760, 920)
    y1 = randint(370, 580)
    x2 = x1+20
    y2 = y1+20
    screen.create_oval(x1, y1, x2, y2, fill=ornaments, outline =ornaments)
#Placed Ornaments
screen.create_oval(840, 330, 860, 350, fill="red", outline ="red")
screen.create_oval(750, 420, 770, 440, fill="green", outline ="green")
screen.create_oval(750, 500, 770, 520, fill="purple", outline ="purple")
screen.create_oval(920, 420, 940, 440, fill="Cyan", outline ="Cyan")
screen.create_oval(920, 500, 940, 520, fill="Orange", outline ="Orange")
screen.create_oval(775, 360, 795, 380, fill="white", outline ="white")
screen.create_oval(815, 380, 835, 400, fill="pink", outline ="pink")
screen.create_oval(855, 360, 875, 380, fill="yellow", outline ="yellow")
screen.create_oval(895, 380, 915, 400, fill="Deep Pink", outline ="Deep Pink")

#Star
screen.create_polygon(810, 310, 850, 300, 890, 310, 870, 280, 890, 260, 860, 260, 850, 240, 840, 260, 810, 260, 830, 280, 810, 310, fill = "yellow", outline = "yellow")

##Penguin
######I realize peguins don't live in the North Pole. This is a magic peguin.

#Body
screen.create_oval(1000, 500, 1150, 700, fill = "black")
screen.create_oval(1020, 520, 1130, 690, fill = "white")

#Head
screen.create_oval(1030, 430, 1120, 510, fill = "black")

#Eyes
screen.create_oval(1045, 442, 1075, 485, fill = "white")
screen.create_oval(1075, 442, 1105, 485, fill = "white")
screen.create_oval(1054, 454, 1066, 467, fill = "black")
screen.create_oval(1084, 454, 1096, 467, fill = "black")

#Nose
screen.create_polygon(1060,485,1090,485,1075,510,1060,485, fill = "orange", smooth="true")

#Flippers
screen.create_polygon(1090, 510, 1130, 570, 1220, 470, 1129, 520, fill="black", smooth="true")
screen.create_polygon(965, 620, 1025, 520, 1045, 530, 995, 620, fill="black", smooth="true")


#Feet
screen.create_oval(1080, 680, 1120, 705, fill="orange")
screen.create_oval(1030, 680, 1070, 705, fill="orange")

screen.update()



