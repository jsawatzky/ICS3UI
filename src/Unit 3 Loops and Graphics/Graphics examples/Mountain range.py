#PROGRAMMER: ADIL IQBAL
#PROGRAM: STILL PICTURE
#DATE MODIFYED: DECEMBER 24,2011
#################################################################################
from random import *
from tkinter import *
inter = Tk()

can = Canvas (inter, width=800, height=800, background="black")
can.pack()

#Creating Grass
can.create_rectangle(0, 600, 800, 800, fill="dark green")

#Creating Moon
can.create_oval(10, 10, 100, 100, fill="white")

#Creating meteor shower
for meteor in range(0,90):
    x = randint(0, 800)
    y = randint(0, 550)

    meteorLength= randint(5,30)
    
    can.create_line(x, y, x+meteorLength, y+meteorLength, fill="white")

#Creating mountains in the background
for mountain in range(0,5):
    x = randint(0, 800)
    can.create_polygon(x, 600, x+100, 300, x+200, 600, fill="dark grey")

#Making the snow top on the mountains    
    can.create_polygon(x+67, 400, x+100, 300, x+150, 450, x+100, 400, x+75, 450, fill="white", outline="black")

#Creating The Big Dipper
can.create_line(300, 200, 340, 180, 365, 200, 400, 225, 465, 230, 460, 245, 455, 260, 425, 260, 400, 225, fill="white", width = 2)
    
    
#Making a sign board
can.create_rectangle(300, 750, 305, 700, fill="black")
can.create_rectangle(350, 750, 355, 700, fill="black")
can.create_rectangle(200, 700, 450, 650, fill="blue")
                    



#Message on the board
can.create_text( 330, 670, text="Chichuwachu Mountains", font="Times 17 italic", fill = "snow")


can.update()


