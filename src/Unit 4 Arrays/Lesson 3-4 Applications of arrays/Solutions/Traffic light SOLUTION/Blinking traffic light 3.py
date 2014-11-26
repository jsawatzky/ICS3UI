from tkinter import *
from random import *
from time import *


root = Tk()
screen = Canvas( root, width=800, height=800, background = "light green" )
screen.pack()

#SPECIAL GUEST FLY-BY
guestImageFile = PhotoImage(file = "images/guest.gif")
airplaneImageFile = PhotoImage(file = "images/airplane.gif")

#SKY
sky = screen.create_rectangle(0, 0, 800, 400, fill = "black", outline="black")


#STARS
for starNum in range(0, 200):
    
    xStar = randint(0, 800)
    yStar = randint(0, 380)
    starSize = randint(1,4)
    
    screen.create_oval(xStar, yStar, xStar+starSize, yStar+starSize, fill="white")


#ROAD   
road = screen.create_polygon(0, 800,  200, 400,  250, 400,  600, 800, fill="grey")
medianStripe = screen.create_polygon( 220, 400,  223, 400,  300, 800, 265, 800, fill="yellow")



#TRAFFIC LIGHT BOX
lamp = screen.create_rectangle(400, 200, 600, 650, fill = "orange")
post = screen.create_rectangle(475, 650, 525, 800, fill = "orange")


#ANIMATION
diameter = 100
yPlane = 100
flightSpeed = 2

colors = [ "green", "yellow", "red" ]
lightHeights = [ 500, 375, 250 ]

for i in range(0, 1000):

    #UPDATE THE AIRPLANE'S POSITION
    
    xPlane = flightSpeed * i - 600
    print(xPlane)
    airplane = screen.create_image( xPlane, yPlane, image = airplaneImageFile )

    #UPDATE THE SPECIAL GUEST'S POSITION
    xGuest = flightSpeed * i - 400
    guest = screen.create_image( xGuest, yPlane, image = guestImageFile )

    #UPDATE THE TOW LINE'S POSITION
    xTowLine1 = xPlane - 20
    xTowLine2 = xGuest + 50
    towLine = screen.create_line( xTowLine1, yPlane, xTowLine2, yPlane, fill = "white" )

    #EVERY 50TH FRAME, CHANGE THE TRAFFIC LIGHT COLOUR
    if i % 10 == 0: 

        #PAINT 3 BLACK DISKS
        for j in range(0,3):
            screen.create_oval(450, lightHeights[j], 550, lightHeights[j]+diameter, fill ="black")


        #PAINT THE COLORED LIGHT ON TOP OF ONE OF THOSE BLACK DISKS
        screen.create_oval(450, lightHeights[i%3], 550, lightHeights[i%3]+diameter, fill = colors[ i % 3 ])




    #UPDATE THE SCREEN, SLEEP AND DELETE
    screen.update()
    sleep(0.01)
    screen.delete( guest, airplane, towLine )
    
