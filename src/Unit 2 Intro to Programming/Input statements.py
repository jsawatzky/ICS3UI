name = input("Enter your name: ")
num = int(input("Enter your favourite positive integer: "))
Object = input("Enter the name of an object: ")

if num > 1:
      message = name + " has " + str(num) + " very large " + Object + "s."

elif num == 1:
      message = name + " has a very large " + Object

elif num == 0:
      message = name + " has no " + Object + "s."

else:
      message = "No negatives allowed."


print(message)
