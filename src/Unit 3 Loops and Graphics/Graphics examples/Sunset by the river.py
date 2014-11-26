##############################
#TITLE:  sunset scenary animation
#This program draws an outdoor scene with moving objects: during a sunset
#Programmer:  Jennifer Kim
#Last modified:  Dec 20, 2011
###############################

from tkinter import *
from random import *

tk = Tk()
me = Canvas(tk, width=900,height=900,background="orange")
me.pack()

#ground
ground = me.create_rectangle(0,450,900,900, fill = "#385E0F", outline = "#385E0F")

#grass
for grass in range(0,15000):
    x = randint(0,900)
    y = randint(450,900)
    
    width = randint(1,5)
    
    me.create_line(x,y,x,y+10, fill="#324F17")
    
#flowers
for flowers1 in range(0,500):
    x = randint(0,900)
    y = randint(450,900)

    width = randint(0,9)

    possibleColour = ["pink", "yellow", "#E32E30", "#8470FF"]
    fColour = choice(possibleColour)
    me.create_oval(x,y, x+5,y+5, width=width, fill=fColour)
    
#small river
me.create_line(-100,900, 100,650, 300,630, 350,600, 400,540, 450,500, 500,480, 550,450, 600,350, 700,300, width=100, fill="blue", smooth="false")


#sky
sky= me.create_rectangle(0,0,900,450, outline="#FF6103", fill = "#FF6103")
    
#sun
me.create_oval(600,350, 1000,600, fill="red", width=2.5, outline="#FF3D0D")

me.create_rectangle(603,450, 900,600, outline="#385E0F", fill="#385E0F")
me.create_rectangle(598,458, 900,630, outline="#385E0F", fill="#385E0F")

for grass in range(0,2000):
    x = randint(600,900)
    y = randint(450,630)
    
    width = randint(1,5)
    
    me.create_line(x,y,x,y+10, fill="yellow")

for flowers in range(0,50):
    x = randint(600,900) 
    y = randint(460,630)

    width = randint(0,9)

    possibleColour = ["pink", "yellow", "#E32E30", "#8470FF"]
    fColour = choice(possibleColour)
    me.create_oval(x,y, x+5,y+5, width=width, fill=fColour)

#cloud
me.create_oval(600,400, 740,420, fill="gray", outline="gray")
me.create_oval(740,420, 950,440, fill="gray", outline="gray")

#forest
for forest in range(0,80):
    x=randint(-30,230)
    y=randint(200,400)

    me.create_oval(x,y, x+100,y+100, fill="darkgreen", outline="darkgreen")
    
#house
#body
me.create_rectangle(10,350,250,500, fill = "#5C3317", outline = "#5C3317")

#roof
me.create_rectangle(50,250, 210,350, fill = "#4B0082", outline="#4B0082")
me.create_polygon(10,350, 50,350, 50,250, fill="#4B0082", outline="#4B0082")
me.create_polygon(210,350, 210,250, 250,350, fill="#4B0082", outline="#4B0082")
me.create_polygon(220,260, 250,260, 250,348, 220,273, fill="#5C3317", outline="black")
me.create_oval(220,230, 250,255, fill="#363636", outline="#363636")
me.create_oval(220+20,230-30, 250+20,255-30, fill="#363636", outline="#363636")
me.create_oval(220+40,230-60, 250+40,255-60, fill="#363636", outline="#363636")


#door
me.create_rectangle(170,390, 230,490, fill = "#9C661F")
me.create_oval(215,440, 225,450, fill = "black", outline = "black")

#window
me.create_rectangle(30,390, 120,430 ,fill="#FFFFCC")

#Pannel
me.create_polygon(270,425, 320,425, 330,440, 320,455, 270,455, fill="brown", outline="brown")
me.create_rectangle(290,450, 300,500, fill="brown", outline="brown")
me.create_text(300,445, fill="lightblue", font="verdana", text="Jen's")

#birds
for birds in range(0,9):
    x = randint(450,700)
    y = randint(300,430)
        
    me.create_line(x,y+10, x,y, x-5,y-5, x-8,y+5, width=3, fill="black")
    me.create_line(x,y+10, x,y, x+5,y-5, x+7,y-5, x+9,y+5, width=3, fill="black")

me.update()














