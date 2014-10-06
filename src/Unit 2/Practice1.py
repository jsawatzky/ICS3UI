'''
Created on Sep 12, 2014

@author: Jacob Sawatzky
'''
index = 0
for i in range(110, 191):
    index +=1
print(index)
# part = input("Which part do you want to do? (1/2/3): ")
# while part != "1" and part != "2" and part != "3":
#     part = input("Invalid! Please type a 1 a 2 or a 3: ")
# part = int(part)
# 
# if part == 1:
#     
#     radius = input("Please enter the radius of the circle: ")
#     valid = False
#     while valid == False:
#         try:
#             radius = float(radius)
#             valid = True
#         except ValueError:
#             radius = input("Invalid! Radius must be a number! Please try again: ")
#     unit = input("Please enter the units (mm/cm/m/km): ")
#     while unit != "mm" and unit != "cm" and unit != "m" and unit != "km":
#         unit = input("Invalid! Please enter mm, cm, m, or km: ")
#         
#     pi = 3.14159
#     
#     area = pi * (radius**2)
#     area = round(area, 1)
#     if area % 1 == 0:
#         area = int(area)
#     
#     print("The area of the circle is " + str(area) + unit + " squared")
#     
# elif part == 2:
#     
#     age = input("Please enter your age: ")
#     valid = False
#     while valid == False:
#         try:
#             age = float(age)
#             valid = True
#         except ValueError:
#             age = input("Invalid! Your age must be a number! Please try again: ")
#     
#     if age >= 19:
#         print("You are old enough to drive, vote and drink alcohol.")
#     elif age >= 18:
#         print("You are old enough to drive and vote.")
#     elif age >= 16:
#         print("You are old enough to drive.")
#     else:
#         print("You are not old enough to do anything.")
# 
# elif part == 3:
#     
#     print("Way to lazy to come up with a mad libs story.")