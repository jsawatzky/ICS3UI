'''
Created on Sep 15, 2014

@author: Jacob Sawatzky
'''

from math import sqrt
from tkinter import *

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
    print("Part 1: Trinomials")
    print("Part 2: Ordinal Numbers")
    print("Part 3: Quadrilateral")
    part = input("Which part would you like to do? (1/2/3): ")
    while part != "1" and part != "2" and part != "3":
        part = input("Invalid! Must be 1, 2 or 3! Please try again: ")
        
    if part == "1": ##Part 1
        
        squared = u"\u00B2"
        
        a = getNum(input("Please enter the A value: "))
        b = getNum(input("Please enter the B value: "))
        c = getNum(input("Please enter the C value: "))
        
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
        
        def orderPoints(points):
         
            lines = doLineCalc(points)
            POIs = {}
            index1 = 0
            for i in ('AB', 'AC', 'AD', 'BC', 'BD', 'CD'):
                index2 = 1
                for j in ('AC', 'AD', 'BC', 'BD', 'CD'):
                    if index1 <= index2:
                        index2 += 1
                        continue
                    POIs[i+j] = {}
                    b = points[i[0]]['y'] - (lines[i] * points[i[0]]['x'])
                    c = points[j[0]]['y'] - (lines[j] * points[j[0]]['x'])
                    if lines[i]['m'] - lines[j]['m'] == 0:
                        POIs[i+j] = "none"
                    else:
                        POIs[i+j]['x'] = (b - c)/(lines[i]['m'] - lines[j]['m'])
                        POIs[i+j]['y'] = (lines[i]['m'] * points[i[0]]['x']) + b
                index1 += 1
            index1 = 0
            for i in ('AB', 'AC', 'AD', 'BC', 'BD', 'CD'):
                index2 = 1
                for j in ('AC', 'AD', 'BC', 'BD', 'CD'):
                    if index1 <= index2:
                        index2 += 1
                        continue
                    if POIs[i+j] == "none":
                        continue
                    notCorner = True
                    for u in range(0, 4):
                        if POIs[i+j]['x'] == points[(i+j)[u]]['x'] and POIs[i+j]['y'] == points[(i+j)[u]]['y']:
                            notCorner = False
                    if notCorner == True:
                        if lines[i]['m'] < lines[j]['m']:
                            
            return points
        
        points = {'A': {}, 'B': {}, 'C': {}, 'D': {}}
        used = []
        for i in ('A', 'B', 'C', 'D'):
            x = getNum(input("Please enter the x for point " + i + ": "))
            y = getNum(input("Please enter the y for point " + i + ": "))
            for j in used:
                while x == points[j]['x'] and y == points[j]['y']:
                    print("You cannot enter two of the same point! Please enter a different cordinate.")
                    x = getNum(input("Please enter the x for point " + i + ": "))
                    y = getNum(input("Please enter the y for point " + i + ": "))
            points[i]['x'] = x
            points[i]['y'] = y
            used.append(i)
        
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
                    lines[i]['l'] = sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
            if lines[i]['l'] < 0:
                lines[i]['l'] *= -1
            lines[i]['M']['x'] = (x1 + x2) / 2
            lines[i]['M']['y'] = (y1 + y2) / 2
          
        if lines['AB']['m'] == lines['BC']['m'] == lines['CD']['m'] == lines['AD']['m']:
            print("The four points form a straight line.")
        elif lines['AB']['m'] == lines['BC']['m'] or lines['AB']['m'] == lines['AD']['m'] or lines['BC']['m'] == lines['CD']['m'] or lines['CD']['m'] == lines['AD']['m']:
            print("The four points a triangle.")
        elif lines['AC']['l'] == lines['BD']['l'] and lines['AC']['M']['x'] == lines['BD']['M']['x'] and lines['AC']['M']['y'] == lines['BD']['M']['y'] and lines['AC']['m'] * lines['BD']['m'] == -1:
            print("The four points form a square.")
            
        img = input("Would you like to see a picture of the shape? (y/n): ")
        while img != "y" and img != "n":
            img = input("Invalid! Please enter a y or an n: ")
        if img == "y":
            myInterface = Tk()
            s = Canvas(myInterface, width=800, height=800, background="white")
            s.pack()
            
            for i in ('A', 'B', 'C', 'D'):
                points[i]['x'] *= -20
                points[i]['y'] *= -20
                points[i]['x'] += 400
                points[i]['y'] += 400
            s.create_polygon(points['A']['x'], points['A']['y'], points['B']['x'], points['B']['y'], points['C']['x'], points['C']['y'], points['D']['x'], points['D']['y'], fill="blue")
            
            done = False
            def buttonCmd():
                global done
                done = True
            button = Button(s, text="Done", command = buttonCmd, anchor = W)
            button.configure(width = 10, activebackground = "green")
            s.create_window(710, 760, anchor = NW, window = button)
            s.update()
            
            while done != True:
                s.update()
            myInterface.destroy()
    
    ##Asks if user wants do do another one
    again = input("Would you like to do another? (y/n): ")
    while again != "y" and again != "n":
        again = input("Invalid! Please enter a y or an n: ")
    if again == "y":
        again = True
    else:
        again = False
