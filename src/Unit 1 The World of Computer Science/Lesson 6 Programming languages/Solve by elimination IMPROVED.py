
A = float( input("Enter the value of A: ") )
B = float( input("Enter the value of B: ") )
C = float( input("Enter the value of C: ") )
D = float( input("Enter the value of D: ") )
E = float( input("Enter the value of E: ") )
F = float( input("Enter the value of F: ") )

print("You have entered the problem: \n")
print("(1)", A, "x +", B, "y =", C)
print("(2)", D, "x +", E, "y =", F, "\n")

if D*B - A*E == 0:
    print( "These two lines are parallel, so there is no solution" )

else:
    y = (D*C - A*F) / (D*B - A*E)
    x = (C - B*y) / A
    print ( "The solution is x =", x, " and y =", y)
