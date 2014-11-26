name = "John A. Macdonald"

iSpace = name.index(" ")
iDot = name.index(".")

firstName = name[ 0 : iSpace ]
middleInitial = name[ iDot - 1 ]
lastName = name[ iDot+2 : len(name) ]

print(firstName)
print(middleInitial)
print(lastName)
