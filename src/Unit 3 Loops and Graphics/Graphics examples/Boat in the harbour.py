from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()

#starz
numStars = 350
numClouds = 20
for starCounter in range(1, numStars+1):
    xStar = randint(0, 800)
    yStar = randint(0, 800)
    size = randint(1,5)
    screen.create_oval( xStar, yStar, xStar+size, yStar+size, fill="white")

    #Clouds
for cloudCounter in range(1, numClouds+1):
    xCloud = randint(350, 450)
    yCloud = randint(150, 250)
    size = randint(20,100)
    screen.create_oval(xCloud, yCloud, xCloud+size, yCloud+size, fill="grey", outline="grey")


#Sun                             
screen.create_oval(0,0, 150, 150,fill="orange")

#water
screen.create_rectangle(0,500, 800, 800,fill="dark blue" ,outline= "light blue", width=10)


#Boat
#Base
screen.create_polygon(100,500, 300,600, 700,600, 800,500, fill="forest green",outline="hot pink",width=10)
#sale
screen.create_polygon(400,480, 600,300, 700,480,fill="white",outline="purple",width=10)
#Line
screen.create_line(600,250,600,500,fill="orange", width=5)
#floating wheels thingys
screen.create_oval(300,500, 400, 600 ,fill="forest green", outline="dark orange", width=16)
#Create a jagged line
screen.create_line( 300, 500,  400, 600,  300, 600,  400, 500,300,500, fill = "orange", width=3, smooth="True")
#TXT
screen.create_text( 550, 550, text="SS OSAMA", font="Times 40 italic bold", fill = "orange")
#Waves
screen.create_line( 0, 600,  100, 700,  200, 600,  300, 700,400,600,500,700,600,600,700,700,800,600, fill = "White", width=3, smooth="True")
#Wave
screen.create_line( 0, 700,  100, 800,  200, 700,  300, 800,400,700,500,800,600,700,700,800,800,700, fill = "White", width=3, smooth="True")
 
screen.update()
