from tkinter import *
from time import *

tk = Tk()
me = Canvas(tk, width=1000,height=1000, background="black")
me.pack()


sideLength = 10
w = 2
delayTime = 0.02
L = [ [10,10] ]

for boxCount in range(1, 10000):

        p = L[0]

        #print ("Current point being extended = " + str(p) + "\n")
        
        pRight = [ p[0] + sideLength, p[1] ]
        pDown =  [ p[0], p[1] + sideLength ]
        
        me.create_line( p[0], p[1], pDown[0],  pDown[1],  fill="red", width = w)
        me.update()
        sleep(delayTime)
        me.create_line( p[0], p[1], pDown[0],  pDown[1],  fill="yellow", width = w)

        me.create_line( p[0], p[1], pRight[0], pRight[1], fill="red", width = w)
        me.update()
        sleep(delayTime)
        me.create_line( p[0], p[1], pRight[0], pRight[1], fill="yellow", width = w)

        L.remove( p )

        if pDown in L:
            L.remove( pDown )
            
        else:
            L.append( pDown )


        if pRight in L:
            L.remove( pRight )
            
        else:
            L.append( pRight )

        #print ("L = " + str(L))

        
        

        

        
        
    
    
