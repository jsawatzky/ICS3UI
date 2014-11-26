###############################################################
#import the Tkinter module, which has functions for making Graphical
#user interfaces
from tkinter import *
from random import*
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()
#creating random stars
for numstars in range(0,400):
    x=randint(0,800)
    y=randint(0,800)
    z=randint(0,6)
    screen.create_oval(x,y,x+z,y+z, fill="gold")


#creating moon
screen.create_oval(675,25,775,125,fill ="#FADA5E")
screen.create_oval(750,50,675,125,fill="black")


#creating random clouds
for numclouds in range(0,5):
    x=randint(0,600)
    y=randint(0,200)
    screen.create_oval(x,y,x+50,y+50,fill="white",outline="white")
    screen.create_oval(x+40,y,x+90,y+50,fill="white",outline="white")
    screen.create_oval(x+80,y,x+130,y+50,fill="white",outline="white")
    screen.create_oval(x+120,y,x+170,y+50,fill="white",outline="white")

#creating lighthouse
screen.create_polygon(50,150,25,125,25,100,50,100,50,50,125,50,125,100,150,100,150,125,125,150, fill ="white",outline="indian red", width = 5)
screen.create_polygon(75,155,75,125,60,100,87.5,75,115,100,100,125,100,155, smooth="true",fill="goldenrod1")
screen.create_rectangle(50,375,125,150, fill="indian red", outline= "indian red")

#creating stripes on lighthouse
screen.create_polygon(50,150,50,175,125,225,125,200, fill="white")
screen.create_polygon(50,225,50,250,125,300,125,275, fill="white")
screen.create_polygon(50,300,50,325,125,375,125,350, fill="white")

#creating cliff
screen.create_polygon(0,370,25,380,33,357,60,365,80,373,87,367,95,354,107,362,120,357,137,367,150,375,175,400,150,425,200,450,175,475,200,485,175,500,225,525,0,550,0,525,0,375, smooth = "true", fill="dark gray",outline="slate gray")




#creating water
screen.create_polygon(0,525,0,800,800,800,800,525, fill="blue")


#creating big boat

screen.create_polygon(450,525,375,325,800,325,800,525,fill="steelblue4")
screen.create_polygon(425,325,475,200,800,200,800,325,fill="ivory")
x=475
y=250
for numwindows in range(0,8):
    screen.create_rectangle(x,y,x+25,y+25, fill="gold",outline="black")
    x=x+50
screen.create_rectangle(500,200,550,125,fill="steelblue4")
screen.create_polygon(500,125,510,100,525,100,540,80,550,80,550,75,565,65,575,65,575,100,550,100,550,125,fill="dark gray",smooth="true")
    

#creating waves
a = 25
c = 50
e = 75
g = 100
for numwaves in range(0,50):
   
    screen.create_line(a,530,c,520,e,530,g,520, fill="blue", smooth = "true", width = 8)

    a= a+25
    c= c+25
    e=e+25
    g=g+25

#creating words on big boat
screen.create_text (525,375, text = "SS Zihan", font = "Times 20 italic bold", fill = "black")
#creating small boat
x=randint(25,325)
y=randint(550,775)
screen.create_polygon(200,625,125,575,325,575,250,625,fill="burlywood")
screen.create_line(125,575,200,625,250,625,325,575,fill="burlywood",smooth="true",width=11)
screen.create_line(125,575,325,575,fill="burlywood",width=6)
screen.create_line(225,575,225,425, width=5)
colour = choice(["red", "green", "purple","hotpink","plum4","orange"])#random sail colours
screen.create_polygon(225,425,225,530,300,530,fill=colour)

###DRAWS A GRID OVERLAY TO HELP YOU PLAN THE SCENE
##spacing = 25
##for x in range(0, 800, spacing): 
##    screen.create_line(x, 10, x, 800, fill="blue")
##    screen.create_text(x, 0, text=str(x), font="Times 8", anchor = N,fill="white")
##
##for y in range(0, 800, spacing):
##    screen.create_line(20, y, 800, y, fill="blue")
##    screen.create_text(0, y, text=str(y), font="Times 8", anchor = W,fill="white")

screen.update()





