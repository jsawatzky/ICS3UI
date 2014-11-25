'''
Created on Oct 23, 2014

@author: Jacob Sawatzky
'''

from tkinter import *

def partA():
    singularNouns = ["Cat", "Dog", "Python", "Chimpanzee"]
    print(singularNouns)
    
    for i in range(0, len(singularNouns)):
        singularNouns[i] += "s"
    print(singularNouns)
    
def partB():
    marks = [47, 91, 76, 51, 50, 45, 60, 73, 86, 46]
    print(marks)
    
    for i in range(0, len(marks)):
        if 46 <= marks[i] <= 49:
            marks[i] = 45
        elif marks[i] == 50:
            marks[i] = 51
    print(marks)
    
def partC():
    tk = Tk()
    s = Canvas(tk, width = 800, height = 800, background = "white")
    s.pack()
    
    points = []
    for i in range(0, 10):
        points.append([])
        points[i].append(int(input("Please enter an x value: ")))
        points[i].append(int(input("Please enter a y value: ")))

    for point in points:
        s.create_oval(point[0]-40, point[1]-40, point[0]+40, point[1]+40, fill = "blue")
        
    while True:
        s.update()