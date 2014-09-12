'''
Created on Sep 12, 2014

@author: Jacob Sawatzky
'''
part = input("Which part do you want to do? (1/2/3): ")
while part != "1" and part != "2" and part != "3":
    part = input("Invalid! Please type a 1 a 2 or a 3: ")
part = int(part)

if part == 1:
    
    radius = input("Please enter the radius of the circle: ")
    valid = False
    while valid == False:
        try:
            radius = float(radius)
            valid = True
        except ValueError:
            radius = input("Invalid! Radius must be a number! Please try again: ")
    unit = input("Please enter the units (mm/cm/m/km): ")
    while unit != "mm" and unit != "cm" and unit != "m" and unit != "km":
        unit = input("Invalid! Please enter mm, cm, m, or km: ")
        
    pi = 3.14159
    
    area = pi * (radius**2)
    area = round(area, 1)
    if area % 1 == 0:
        area = int(area)
    
    print("The area of the circle is " + str(area) + unit + " squared")
    
elif part == 2:
    
    pass

elif part == 3:
    
    pass