# REVIEW OF MODULAR ARITHMETIC USING THE OPERATOR %

# A % B means "the remainder when A is divided by B"

print("X" + "\t" + "X / 5" + "\t" + "X % 5")
print("--------------------------")

for x in range(0, 26):
    
    xDivBy5 = x / 5
    xMod5   = x % 5
    
    print( str( x ) + "\t" + str( xDivBy5 ) + "\t" + str( xMod5 ))
    



    
