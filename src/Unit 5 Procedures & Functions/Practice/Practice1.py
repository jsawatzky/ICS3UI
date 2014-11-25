'''
Created on Nov 13, 2014

@author: sawaj6311
'''

from math import pi

# def getInt(numStr):
#     valid = False
#     while valid == False:
#         try:
#             numInt = int(numStr)
#             valid = True
#         except ValueError:
#             try:
#                 numFloat = float(numStr)
#                 numStr = input("You must enter an integer value! (No decimals) Please try again: ")
#             except ValueError:
#                 numStr = input("You must enter a number! Please try again: ")
#     return numInt
# 
# 
# 
# def cylinderVolume(r, h): return (2*pi*(r**2))*h
# 
# radius = getInt(input("Please enter the radius of the cylinder: "))
# height = getInt(input("Please enter the height of the cylinder: "))
# 
# print("The volume of the cylinder is: " + str(round(cylinderVolume(radius, height), 2)))
# 
# def getSlope(x1, y1, x2, y2):
#     try:
#         slope = round((y2-y1)/(x2-x1), 2)
#     except:
#         slope = "undefined"
#     return slope
# 
# x1 = getInt(input("Please enter the first x value: "))
# y1 = getInt(input("Please enter the first y value: "))
# x2 = getInt(input("Please enter the second x value: "))
# y2 = getInt(input("Please enter the second y value: "))
# 
# print("The slope of the line is " + str(getSlope(x1, y1, x2, y2)))
# 
# def ordinal(num):
#                 
#     num = str(num)
#     numChar = len(num)
#     lastChar = num[numChar - 1]
#            
#     ending = ""
#     if lastChar == "1":
#         if num[numChar - 2] != "1" or numChar == 1:
#             ending = "st"
#     elif lastChar == "2":
#         if num[numChar - 2] != "1":
#             ending = "nd"
#     elif lastChar == "3":
#         if num[numChar - 2] != "1":
#             ending = "rd"
#             
#     if ending == "":
#         ending = "th"
#             
#     return num + ending
# 
# for i in range(1, 101):
#     print("Ordinal number of " + str(i) + " is: " + ordinal(i))

def getCircleArea(r): return pi*r**2

def getTriangleArea(b, h): return (b*h)/2

def getRectangleArea(l, w): return l*w









