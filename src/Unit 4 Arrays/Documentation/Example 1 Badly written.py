a=input("Enter a: ")
e=input("Enter e: ")
c=input("Enter c: ")
d=input("Enter d: ")
if a==c:
    print("The line is vertical.  Its equation is x = " + str(a))
elif e==d:
    print("The line is horizontal.  Its equation is y = " + str(e))
else:  
    y3=float(d-e)
    x3=float(c-a)
    zzz17=y3/x3
    if zzz17==1:
        x4="x"
    elif zzz17==-1:
        x4="-x"
    else:
        x4=str(zzz17)+"x"
    b=c-zzz17*a
    stuff="The equation of the line is y = "+x4
    if b > 0:
        stuff2=" + "+str(b)
    elif b < 0:
        stuff2=str(b)
    else:
        stuff2="" 
    print(stuff+stuff2)
