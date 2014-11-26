import turtle
nino = turtle.Pen()


x = 100

nino.width(20)
nino.speed(2)
nino.color("red")


for counter in range(0,10):
    
    nino.forward( x )
    nino.right(85)

    x = x + 20

    
    
