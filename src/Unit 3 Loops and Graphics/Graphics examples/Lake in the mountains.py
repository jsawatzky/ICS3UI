from tkinter import *
from random import *
from time import *
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background= "#87CEEB")
screen.pack()

#Ground
ground  = screen.create_rectangle (0, 300, 800,800, fill = "#74C365")

#Mountains
screen.create_polygon (80,220, 120,210, 150,200, 155,205, 225,185, 248,175, 270,200, 275,196, 310,210, 400,140, 470,110, 600,170, 635,200, 665,180, 685,172, 800,150,800,300, 150,300, 80,220, fill = "#355E3B",)
screen.create_polygon (250, 300, 148,260, 98,225, 50,200, 0,150, 0,315, 50,305, 80,303, 125,300,  250,300, fill = "#355E3B",)

#Trees on closest mountain
for trees in range (0, 500):
    x = randint (0, 100)
    y = randint (220, 300)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")
    
for trees in range (0, 20):
    x = randint (0, 40)
    y = randint (300, 310)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")

for trees in range (0, 50):
    x = randint (0, 40)
    y = randint (180, 220)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")

for trees in range (0, 150):
    x = randint (100, 130)
    y = randint (240, 300)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")

for trees in range (0, 100):
    x = randint (130, 160)
    y = randint (255, 300)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")

for trees in range (0, 50):
    x = randint (160, 175)
    y = randint (265, 300)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")

for trees in range (0, 50):
    x = randint (175, 190)
    y = randint (275, 300)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")
    
for trees in range (0, 15):
    x = randint (190, 202)
    y = randint (285, 300)

    width = randint(0,5)

    screen.create_polygon(x,y, x-3,y-5, x-6,y, x,y ,width = width, fill = "#014421")
#Make loch
screen.create_polygon (-50,650, 150,625, 250,600, 350,575, 450,550, 550,525, 600,465, 590,420, 580,350, 625,335, 650,300, 200,300, 100,301, 50,304, -30,315, -50,650, fill="#417DC1", smooth="true")
screen.create_polygon (510,300, 725,300, 723,310, 724,310, 750,310, 600,310, 510,300, fill = "#417DC1")


#Make sand
for sand in range (0,1000):
    x = randint (0, 100)
    y = randint (640, 700)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,1000):
    x = randint (100, 175)
    y = randint (630, 695)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,900):
    x = randint (170, 225)
    y = randint (623, 688)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,900):
    x = randint (220, 275)
    y = randint (615, 680)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,900):
    x = randint (270, 315)
    y = randint (605, 670)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,900):
    x = randint (310, 370)
    y = randint (590, 660)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,1200):
    x = randint (355, 450)
    y = randint (575, 648)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,1200):
    x = randint (445, 550)
    y = randint (560, 620)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,1200):
    x = randint (530,630 )
    y = randint (540, 603 )

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,2000):
    x = randint (590,750)
    y = randint (475,550)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,3000):
    x = randint (580,740)
    y = randint (385,480)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,2000):
    x = randint (580,735)
    y = randint (340,390)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,200):
    x = randint (560,595)
    y = randint (515,545)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,50):
    x = randint (575,590)
    y = randint (495,516)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,100):
    x = randint (485,520)
    y = randint (545,565)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")

for sand in range (0,1000):
    x = randint (635,725)
    y = randint (307,345)

    screen.create_oval (x,y, x+2,y+2, fill = "#C2B280")
    
#Create shoreline
width = 45
screen.create_oval (570,380, 607,400, fill ="#417DC1", outline="#417DC1")
screen.create_line (0,640, 140,635, 150,627, 200,624, 250,610, 300,607, 350,595, 400,587, 450,565, 500,550, 550,542, 575,520, 590,507, 580,475, 590,425,600,400,fill= "#417DC1", smooth="true", width = width) 
screen.create_oval (615,308, 640,335, outline ="#417DC1", fill = "#417DC1")
screen.create_oval (605,335, 625,335, outline ="#417DC1", fill = "#417DC1")
screen.create_line (635,308, 700,310, 727,308, width = 10 , fill = "#417DC1")

#Create grass
for grass in range (0,250):
    x = randint (200,375)
    y = randint (680,750)

    screen.create_line (x,y, x-10,y-12, x-15,y-25, fill="#E4D96F", smooth = "true")

for grass in range (0,20):
    x = randint (0,150)
    y = randint (710,800)

    screen.create_line (x,y, x-10,y-12, x-15,y-25, fill="#E4D96F", smooth = "true")

for grass in range (0,100):
    x = randint (375,500)
    y = randint (660,710)

    screen.create_line (x,y, x-10,y-12, x-15,y-25, fill="#E4D96F", smooth = "true")    

for grass in range (0,100):
    x = randint (450,575)
    y = randint (635,680)

    screen.create_line (x,y, x-10,y-12, x-15,y-25, fill="#E4D96F", smooth = "true")
for grass in range (0,100):
    x = randint (565,660)
    y = randint (600,655)

    screen.create_line (x,y, x-10,y-12, x-15,y-25, fill="#E4D96F", smooth = "true")    
for grass in range (0,100):
    x = randint (620,750)
    y = randint (545,610)

    screen.create_line (x,y, x-10,y-12, x-15,y-25, fill="#E4D96F", smooth = "true")

for grass in range (0,100):
    x = randint (770,800)
    y = randint (445,570)


    screen.create_line (x,y, x-10,y-12, x-15,y-25, fill="#E4D96F", smooth = "true")
    
for grass in range (0,400):
    x = randint (760,800)
    y = randint (305,440)

    screen.create_line (x,y, x-5,y-6, x-10,y-13, fill="#E4D96F", smooth = "true")    
#Create bank
screen.create_polygon (697,320, 700,306, 720,298, 760,293, 760,450, 755,500, 753,548, 740,550, 730,400, 710,310, fill = "#1E4D2B", smooth = "true")

#Create sign
screen.create_rectangle (515,660, 665,710, fill = "white", outline = "black")
screen.create_line (565,710, 565,750, width = 10, fill = "black")
screen.create_line (615,710, 615,750, width = 10, fill = "black")
screen.create_text (590,685, text = "Loch Katrine", font = "Helvetica 14", fill = "black")

#ANIMATION

for a in range (0,1500):
    #Parameters
    stickman1X = 215 + a/2 +sin(a)
    stickman1Y = 170
    stickman2X = 165 + a/1.5 +sin(a)
    stickman2Y = 150
    stickmanSize = 50
    headDiameter = 0.2 * stickmanSize
    bodyLength = 0.4 * stickmanSize
    legLength = 0.3 * stickmanSize
    armLength = legLength / 2
    balloon1x = 200 + a /2 + sin(a)
    balloon1y = 60
    balloon2x = 150 + a /1.5 + sin(a)
    balloon2y = 40
    balloondiameter=80
    #Draw

    #Balloons
    balloon = screen.create_oval(balloon1x,balloon1y, balloon1x+balloondiameter,balloon1y+balloondiameter,fill="blue")
    string1 = screen.create_line(balloon1x+30,balloon1y+balloondiameter, balloon1x+30,balloon1y+balloondiameter*2,fill="black")
    string2 = screen.create_line(balloon1x+45,balloon1y+balloondiameter, balloon1x+45,balloon1y+balloondiameter*2,fill="black")
    basket = screen.create_rectangle(balloon1x+15, balloon1y+balloondiameter*2,balloon1x+70, balloon1y+120,fill="orange")
    stickmanhead = screen.create_oval(stickman1X, stickman1Y, stickman1X+headDiameter,stickman1Y+headDiameter, fill = "black")
    stickmanleftarm = screen.create_line(stickman1X+headDiameter/2,stickman1Y+headDiameter/2+bodyLength/3, stickman1X+headDiameter/2-14,stickman1Y+headDiameter/2-bodyLength/2-armLength,fill="black", width=5)                      
    stickmanrightarm = screen.create_line(stickman1X+headDiameter/2,stickman1Y+headDiameter/2+bodyLength/3, stickman1X+headDiameter/2+14,stickman1Y+headDiameter/2-bodyLength/2-armLength,fill="black", width=5)

    

    balloon2 = screen.create_oval(balloon2x,balloon2y, balloon2x+balloondiameter,balloon2y+balloondiameter,fill="blue")
    string1II = screen.create_line(balloon2x+30,balloon2y+balloondiameter, balloon2x+30,balloon2y+balloondiameter*2,fill="black")
    string2II = screen.create_line(balloon2x+45,balloon2y+balloondiameter, balloon2x+45,balloon2y+balloondiameter*2,fill="black")
    basket2 = screen.create_rectangle(balloon2x+15, balloon2y+balloondiameter*2,balloon2x+70, balloon2y+120,fill="orange")
    stickmanhead2 = screen.create_oval(stickman2X, stickman2Y, stickman2X+headDiameter,stickman2Y+headDiameter, fill = "black")
    stickmanleftarm2 = screen.create_line(stickman2X+headDiameter/2,stickman2Y+headDiameter/2+bodyLength/3, stickman2X+headDiameter/2-14,stickman2Y+headDiameter/2-bodyLength/2-armLength,fill="black", width=5)                      
    stickmanrightarm2 = screen.create_line(stickman2X+headDiameter/2,stickman2Y+headDiameter/2+bodyLength/3, stickman2X+headDiameter/2+14,stickman2Y+headDiameter/2-bodyLength/2-armLength,fill="black", width=5)
    
    screen.update()
    sleep(0.001)
    screen.delete(balloon, string1, string2, basket, stickmanhead, stickmanleftarm, stickmanrightarm, balloon2, string1II, string2II, basket2, stickmanhead2, stickmanleftarm2, stickmanrightarm2)
    
for b in range (0,2000):
    #Parameters
    boatx = 100 + b/2
    boaty = 350 + sin(b)
    boatlength = 100

    if boatx <600:
        mainbody = screen.create_polygon(boatx,boaty, boatx-25,boaty+20, boatx-45,boaty+50, boatx-boatlength,boaty+50, boatx-105,boaty+10, boatx-104,boaty, boatx,boaty,fill="grey")
        mast = screen.create_line(boatx-30,boaty, boatx-30,boaty-80,fill="black",width=10)
        sail1 = screen.create_polygon(boatx-30,boaty-80, boatx-100,boaty-15,boatx-30,boaty-5, boatx-30,boaty-80,fill="white")
        sail2 = screen.create_polygon (boatx-30,boaty-80, boatx-26,boaty-60,boatx-28,boaty-30,boatx-31,boaty-5,boatx-15,boaty-15,boatx-5,boaty-5,boatx,boaty-20,boatx-10,boaty-40,boatx-20,boaty-50,boatx-25,boaty-60,boatx-30,boaty-80,fill="white",smooth="true")
        flag = screen.create_rectangle(boatx-70,boaty-80,boatx-30,boaty-65,fill="#000080")
        text = screen.create_text(boatx-50,boaty-73,text="SCOTLAND",font="Helvetica 5",fill="white")
        
    
        screen.update()
        sleep(0.01)
        screen.delete(mainbody, mast, sail1, sail2, flag, text)
        

            


    







#GRID OVERLAY
                
##spacing = 50
##for x in range(0, 800, spacing): 
##    screen.create_line(x, 10, x, 800, fill="blue")
##    screen.create_text(x, 0, text=str(x), font="Times 8", anchor = N)
##
##for y in range(0, 800, spacing):
##    screen.create_line(20, y, 800, y, fill="blue")
##    screen.create_text(0, y, text=str(y), font="Times 8", anchor = W)
##
##screen.update()

##x,y, x,y-5, x-3,y-5, x,y-9, x+3,y-5, x,y-5, x,y,
