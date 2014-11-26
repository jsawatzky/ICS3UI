#INPUT THE PROBLEM
print("Welcome to the linear system solver! \n")
print("Enter a problem of the form:")
print("Ax + By = C")
print("Dx + Ey = F \n")

A = float( input("Enter the value of A: ") )
B = float( input("Enter the value of B: ") )
C = float( input("Enter the value of C: ") )
D = float( input("Enter the value of D: ") )
E = float( input("Enter the value of E: ") )
F = float( input("Enter the value of F: ") )

print("You have entered the problem: \n")
print("(1)" + str( A) + "x +" + str(B) + "y =" + str( C))
print("(2)" + str( D) + "x +" + str(E) + "y =" + str(F) + "\n")


#CALCULATE THE SOLUTION
y = (D*C - A*F) / (D*B - A*E)
x = (C - B*y) / A


#OUTPUT THE RESULT
print ( "The solution is x =" + str( x ) + " and y =" + str(y))
