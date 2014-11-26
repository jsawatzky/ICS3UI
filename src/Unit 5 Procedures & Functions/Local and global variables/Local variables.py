
x=100

def doSomething( newValue ):
    x = newValue #Here, x is a new local variable. Not the same as x above
    print(x)

doIt( 20 )
print(x) #x refers to the global value.

