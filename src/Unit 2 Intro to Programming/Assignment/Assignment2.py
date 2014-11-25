'''
Created on Sep 15, 2014

@author: Jacob Sawatzky
'''

from math import sqrt
from tkinter import *
from tkinter.constants import NE, NW

##Gets the integer version of a string
def getInt(numStr):
    valid = False
    while valid == False:
        try:
            numInt = int(numStr)
            valid = True
        except ValueError:
            try:
                numFloat = float(numStr)
                numStr = input("You must enter an integer value! (No decimals) Please try again: ")
            except ValueError:
                numStr = input("You must enter a number! Please try again: ")
    return numInt

##Gets the float version of a string
def getNum(numStr):
    valid = False
    while valid == False:
        try:
            num = float(numStr)
            valid = True
        except ValueError:
            numStr = input("You must enter a number! Please try again: ")
    return num

again = True
while again == True: 
    ##Asks which part the user wants to do
    print("Assignment 2:")
    print("Part 1: Trinomial")
    print("Part 2: Ordinal")
    print("Part 3: Quadrilateral")
    part = input("Which part would you like to do? (1/2/3): ")
    while part != "1" and part != "2" and part != "3":
        part = input("Invalid! Must be 1, 2 or 3! Please try again: ")
        
    if part == "1": ##Part 1
        
        squared = u"\u00B2"
        
        a = getNum(input("Please enter the A value: "))
        b = getNum(input("Please enter the B value: "))
        c = getNum(input("Please enter the C value: "))

        #Removes the ".0"
        if a % 1 == 0:
            a = int(a)
        if b % 1 == 0:
            b = int(b)
        if c % 1 == 0:
            c = int(c)
        
        exp = "The formated expression is: "
        
        ##Gets the A part
        if a == -1:
            exp += "-x" + squared
        elif a == 1:
            exp += "x" + squared
        elif a < -1 or a > 1:
            exp += str(a) + "x" + squared
        else:
            pass
        ##Gets the B part
        if b == -1:
            exp += "-x"
        elif b == 1:
            if a == 0:
                exp += "x"
            else:
                exp += "+x"
        elif b < -1:
            exp += str(b) + "x"
        elif b > 1:
            if a == 0:
                exp += str(b) + "x"
            else:
                exp += "+" + str(b) + "x"
        else:
            pass
        ##Gets the C part
        if c < -1:
            exp += str(c)
        elif c > 1:
            if a == 0 and b == 0:
                exp += str(c)
            else:
                exp += "+" + str(c)
        else:
            pass

        if exp == "The formated expression is: ":
            exp += "0"
        
        print(exp)
    
    elif part == "2": ##Part 2
        
        numInt = getInt(input("Please enter a number: "))
        while numInt < 1 or numInt > 100:
            numInt = getInt(input("Invalid! Please enter a number in between 1 and 100: "))
        num = str(numInt)
                
        numChar = len(num)
        lastChar = num[numChar - 1]
           
        if lastChar == "1":
            if num[numChar - 2] != "1":
                ending = "st"
        elif lastChar == "2":
            if num[numChar - 2] != "1":
                ending = "nd"
        elif lastChar == "3":
            if num[numChar - 2] != "1":
                ending = "rd"
        else:
            ending = "th"
            
        print("The ordinal is: " + num + ending)
        
    else: ##Part 3

        #Does all calculations with the line (slope, length, midpoint)
        def doLineCalc(points):
            
            lines = {'AB': {'M': {}}, 'AC': {'M': {}}, 'AD': {'M': {}}, 'BC': {'M': {}}, 'BD': {'M': {}}, 'CD': {'M': {}}}
            for i in ('AB', 'AC', 'AD', 'BC', 'BD', 'CD'):
                x1 = points[i[0]]['x']
                y1 = points[i[0]]['y']
                x2 = points[i[1]]['x']
                y2 = points[i[1]]['y']
                if x1 == x2:
                    lines[i]['m'] = "u"
                    lines[i]['l'] = x2 - x1
                else:
                    lines[i]['m'] = (y2 - y1) / (x2 - x1)
                    if y1 == y2:
                        lines[i]['l'] = y2 - y1
                    else:
                        lines[i]['l'] = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
                if lines[i]['l'] < 0:
                    lines[i]['l'] *= -1
                lines[i]['M']['x'] = (x1 + x2) / 2
                lines[i]['M']['y'] = (y1 + y2) / 2
            return lines

        #Utility fuction to get the highest, lowest, left most, right most point from 2
        def getCorrectPoint(point1, point2, direction):
            
            if direction == "high":
                if point1['y'] > point2['y']:
                    return point1
                else:
                    return point2
            elif direction == "low":
                if point1['y'] < point2['y']:
                    return point1
                else:
                    return point2
            elif direction == "right":
                if point1['x'] > point2['x']:
                    return point1
                else:
                    return point2
            else:
                if point1['x'] < point2['x']:
                    return point1
                else:
                    return point2

        #Orders all points in a clockwise patter
        def orderPoints(points):
         
            orgPoints = {'A': {}, 'B': {}, 'C': {}, 'D': {}}
            lines = doLineCalc(points)
            POIs = {}
            index = 0
            for i in ('AB', 'AC', 'AD', 'BC', 'BD', 'CD'):
                index2 = 0
                for j in ('AC', 'AD', 'BC', 'BD', 'CD'):
                    if index > index2:
                        index2 += 1
                        continue
                    POIs[i+j] = {}
                    if lines[i]['m'] == "u" and lines[j]['m'] == "u":
                        POIs[i+j] = "none"
                    elif lines[i]['m'] == "u":
                        POIs[i+j]['x'] = points[i[0]]['x']
                        b = points[j[0]]['y'] - (lines[j]['m'] * points[j[0]]['x'])
                        POIs[i+j]['y'] = (lines[j]['m'] * POIs[i+j]['x']) + b
                    elif lines[j]['m'] == "u":
                        POIs[i+j]['x'] = points[j[0]]['x']
                        b = points[i[0]]['y'] - (lines[i]['m'] * points[i[0]]['x'])
                        POIs[i+j]['y'] = (lines[i]['m'] * POIs[i+j]['x']) + b
                    else:
                        b = points[i[0]]['y'] - (lines[i]['m'] * points[i[0]]['x'])
                        c = points[j[0]]['y'] - (lines[j]['m'] * points[j[0]]['x'])
                        if lines[i]['m'] == lines[j]['m']:
                            POIs[i+j] = "none"
                        else:
                            POIs[i+j]['x'] = (b - c)/(lines[j]['m'] - lines[i]['m'])
                            POIs[i+j]['y'] = (lines[i]['m'] * POIs[i+j]['x']) + b
                            POIs[i+j]['x'] = round(POIs[i+j]['x'], 0)
                            POIs[i+j]['y'] = round(POIs[i+j]['y'], 0)
                index += 1
            
            index = 0
            for i in ('AB', 'AC', 'AD', 'BC', 'BD', 'CD'):
                index2 = 0
                for j in ('AC', 'AD', 'BC', 'BD', 'CD'):
                    if index > index2:
                        index2 += 1
                        continue
                    if POIs[i+j] == "none":
                        continue
                    valid = True
                    for u in range(0, 4):
                        if POIs[i+j]['x'] == points[(i+j)[u]]['x'] and POIs[i+j]['y'] == points[(i+j)[u]]['y']:
                            valid = False
                    counterXb = 0
                    counterXs = 0
                    counterYb = 0
                    counterYs = 0
                    for u in range(0, 4):
                        if POIs[i+j]['x'] > points[(i+j)[u]]['x']:
                            counterXb += 1
                        if POIs[i+j]['y'] > points[(i+j)[u]]['y']:
                            counterYb += 1
                        if POIs[i+j]['x'] < points[(i+j)[u]]['x']:
                            counterXs += 1
                        if POIs[i+j]['y'] < points[(i+j)[u]]['y']:
                            counterYs += 1
                    if counterXb == 4 or counterXs == 4 or counterYb == 4 or counterYs == 4:
                        valid = False
                    if valid == True:
                        if lines[i]['m'] == "u" and lines[j]['m'] <= 0:
                            orgPoints['A'] = getCorrectPoint(points[j[0]], points[j[1]], "left")
                            orgPoints['B'] = getCorrectPoint(points[i[0]], points[i[1]], "high")
                            orgPoints['C'] = getCorrectPoint(points[j[0]], points[j[1]], "right")
                            orgPoints['D'] = getCorrectPoint(points[i[0]], points[i[1]], "low")
                        elif lines[j]['m'] == "u" and lines[i]['m'] <= 0:
                            orgPoints['A'] = getCorrectPoint(points[i[0]], points[i[1]], "left")
                            orgPoints['B'] = getCorrectPoint(points[j[0]], points[j[1]], "high")
                            orgPoints['C'] = getCorrectPoint(points[i[0]], points[i[1]], "right")
                            orgPoints['D'] = getCorrectPoint(points[j[0]], points[j[1]], "low")
                        elif lines[i]['m'] == "u" and lines[j]['m'] >= 0:
                            orgPoints['A'] = getCorrectPoint(points[i[0]], points[i[1]], "high")
                            orgPoints['B'] = getCorrectPoint(points[j[0]], points[j[1]], "left")
                            orgPoints['C'] = getCorrectPoint(points[i[0]], points[i[1]], "low")
                            orgPoints['D'] = getCorrectPoint(points[j[0]], points[j[1]], "right")
                        elif lines[j]['m'] == "u" and lines[i]['m'] >= 0:
                            orgPoints['A'] = getCorrectPoint(points[j[0]], points[j[1]], "high")
                            orgPoints['B'] = getCorrectPoint(points[i[0]], points[i[1]], "left")
                            orgPoints['C'] = getCorrectPoint(points[j[0]], points[j[1]], "low")
                            orgPoints['D'] = getCorrectPoint(points[i[0]], points[i[1]], "right")
                        elif lines[i]['m'] > lines[j]['m']:
                            orgPoints['A'] = getCorrectPoint(points[j[0]], points[j[1]], "left")
                            orgPoints['B'] = getCorrectPoint(points[i[0]], points[i[1]], "high")
                            orgPoints['C'] = getCorrectPoint(points[j[0]], points[j[1]], "right")
                            orgPoints['D'] = getCorrectPoint(points[i[0]], points[i[1]], "low")
                        else:
                            orgPoints['A'] = getCorrectPoint(points[i[0]], points[i[1]], "high")
                            orgPoints['B'] = getCorrectPoint(points[j[0]], points[j[1]], "right")
                            orgPoints['C'] = getCorrectPoint(points[i[0]], points[i[1]], "low")
                            orgPoints['D'] = getCorrectPoint(points[j[0]], points[j[1]], "left")
                index += 1
                            
            return orgPoints

        #Gets points from users
        points = {'A': {}, 'B': {}, 'C': {}, 'D': {}}
        used = []
        for i in ('A', 'B', 'C', 'D'):
            x = getInt(input("Please enter the x for point " + i + ": "))
            y = getInt(input("Please enter the y for point " + i + ": "))
            for j in used:
                while x == points[j]['x'] and y == points[j]['y']:
                    print("You cannot enter two of the same point! Please enter a different cordinate.")
                    x = getInt(input("Please enter the x for point " + i + ": "))
                    y = getInt(input("Please enter the y for point " + i + ": "))
            points[i]['x'] = x
            points[i]['y'] = y
            used.append(i)
        
        points = orderPoints(points)
        lines = doLineCalc(points)
        
        prefix = "The four points form a "

        #Utility funcution to check is two lines are perpendicular
        def perpendicular(m1, m2):
            
            if m1 == "u" and m2 == 0:
                return True
            elif m2 == "u" and m1 == 0:
                return True
            elif m1 * m2 == -1:
                return True
            else:
                return False

        if lines['AB']['m'] == lines['BC']['m'] == lines['CD']['m'] == lines['AD']['m']: #Straight line
            print(prefix + "straight line.")
        elif lines['AB']['m'] == lines['BC']['m'] or lines['AB']['m'] == lines['AD']['m'] or lines['BC']['m'] == lines['CD']['m'] or lines['CD']['m'] == lines['AD']['m']: #Triangle
            print(prefix + "triangle.")
        elif lines['AC']['l'] == lines['BD']['l'] and lines['AC']['M']['x'] == lines['BD']['M']['x'] and lines['AC']['M']['y'] == lines['BD']['M']['y'] and perpendicular(lines['AC']['m'], lines['BD']['m']): #Square
            print(prefix + "square.")
        elif lines['AB']['l'] == lines['BC']['l'] == lines['CD']['l'] == lines['AD']['l']: #Rhombus
            print(prefix + "rhombus.")
        elif (lines['AB']['m'] == lines['CD']['m'] and lines['AD']['l'] == lines['BC']['l']) and perpendicular(lines['AB']['m'], lines['AD']['m']): #Rectangle
            print(prefix + "rectangle.")
        elif perpendicular(lines['AC']['m'], lines['BD']['m']): #Kite
            counter = 0
            if lines['AB']['l'] == lines['AD']['l']:
                counter += 1
            if lines['AB']['l'] == lines['BC']['l']:
                counter += 1
            if lines['BC']['l'] == lines['CD']['l']:
                counter += 1
            if lines['CD']['l'] == lines['AD']['l']:
                counter += 1
            if counter == 2:
                print(prefix + "kite.")
        elif lines['AB']['m'] == lines['CD']['m'] and lines['AD']['m'] == lines['BC']['m']: #Parallelogram
            print(prefix + "parallelogram.")
        elif lines['AB']['m'] == lines['CD']['m'] or lines['AD']['m'] == lines['BC']['m']: #Trapezoid
            print(prefix + "trapezoid")
        else: #Quadrilateral
            print(prefix + "boring old quadrilateral.")

        #Shows a graphic of the shape
        img = input("Would you like to see a picture of the shape? (y/n): ")
        while img != "y" and img != "n":
            img = input("Invalid! Please enter a y or an n: ")
        if img == "y":
            myInterface = Tk()
            s = Canvas(myInterface, width=800, height=800, background="white")
            s.pack()
            
            for i in ('A', 'B', 'C', 'D'):
                points[i]['x'] *= 25
                points[i]['y'] *= -25
                points[i]['x'] += 400
                points[i]['y'] += 400
            s.create_line(400, 0, 400, 800, fill="black")
            s.create_line(0, 400, 800, 400, fill="black")
            s.create_polygon(points['A']['x'], points['A']['y'], points['B']['x'], points['B']['y'], points['C']['x'], points['C']['y'], points['D']['x'], points['D']['y'], fill="blue")
            s.create_oval(points['A']['x']-3, points['A']['y']-3, points['A']['x']+3, points['A']['y']+3, fill="red")
            s.create_text(points['A']['x'], points['A']['y'], text = "(" + str(int((points['A']['x']-400)/25)) + ", " + str(int((points['A']['y']-400)/(-25))) + ")", font="Times 12", anchor = SE)
            s.create_oval(points['B']['x']-3, points['B']['y']-3, points['B']['x']+3, points['B']['y']+3, fill="red")
            s.create_text(points['B']['x'], points['B']['y'], text = "(" + str(int((points['B']['x']-400)/25)) + ", " + str(int((points['B']['y']-400)/(-25))) + ")", font="Times 12", anchor = SW)
            s.create_oval(points['C']['x']-3, points['C']['y']-3, points['C']['x']+3, points['C']['y']+3, fill="red")
            s.create_text(points['C']['x'], points['C']['y'], text = "(" + str(int((points['C']['x']-400)/25)) + ", " + str(int((points['C']['y']-400)/(-25))) + ")", font="Times 12", anchor = NW)
            s.create_oval(points['D']['x']-3, points['D']['y']-3, points['D']['x']+3, points['D']['y']+3, fill="red")
            s.create_text(points['D']['x'], points['D']['y'], text = "(" + str(int((points['D']['x']-400)/25)) + ", " + str(int((points['D']['y']-400)/(-25))) + ")", font="Times 12", anchor = NE)
            done = False
            def buttonCmd():
                global done
                done = True
            button = Button(s, text="Done", command = buttonCmd, anchor = W)
            button.configure(width = 10, activebackground = "green")
            s.create_window(710, 760, anchor = NW, window = button)
            s.update()
            
            while done != True:
                try:
                    s.update()
                except:
                    done = True
            try:
                myInterface.destroy()
            except:
                pass
    
    ##Asks if user wants do do another one
    again = input("Would you like to do another? (y/n): ")
    while again != "y" and again != "n":
        again = input("Invalid! Please enter a y or an n: ")
    if again == "y":
        again = True
    else:
        again = False
