'''
Created on Nov 20, 2014

@author: Jacob Sawatzky
'''

from tkinter import *
from datetime import *

def grid(s, width, height, spacing):
    for x in range(0, width, spacing): 
        s.create_line(x, 10, x, height, fill="magenta")
        s.create_text(x, 0, text=str(x), font="Times 8", anchor = N, fill="magenta")
    for y in range(0, height, spacing):
        s.create_line(20, y, width, y, fill="magenta")
        s.create_text(0, y, text=str(y), font="Times 8", anchor = W, fill="magenta")

ones = {'0': "",
        '1': "One ",
        '2': "Two ",
        '3': "Three ",
        '4': "Four ",
        '5': "Five ",
        '6': "Six ",
        '7': "Seven ",
        '8': "Eight ",
        '9': "Nine "}
tens = {'0': "and ",
        '1': {'0': "Ten ",
              '1': "Eleven ",
              '2': "Twelve ",
              '3': "Thirteen ",
              '4': "Fourteen ",
              '5': "Fifteen ",
              '6': "Sixteen ",
              '7': "Seventeen ",
              '8': "Eighteen ",
              '9': "Nineteen "},
        '2': "Twenty ",
        '3': "Thirty ",
        '4': "Fourty ",
        '5': "Fifty ",
        '6': "Sixty ",
        '7': "Seventy ",
        '8': "Eighty ",
        '9': "Ninety "}
ext = {0: "",
       1: "Thousand ",
       2: "Million ",
       3: "Billion ",
       4: "Trillion ",
       5: "Quadrillion ",
       6: "Quintillion ",
       7: "Sextillion ",
       8: "Septillon ",
       9: "Octillion ",
       10: "Nonillion "}

def getStrNum(num):
    string = ""
    if len(num) == 3:
        if num[0] != "0":
            string += ones[num[0]] + "Hundred "
        if num[1] == '1':
            string += tens['1'][num[2]]
            return string
        else:
            string += tens[num[1]]
            string += ones[num[2]]
    elif len(num) == 2:
        if num[0] == '1':
            string += tens['1'][num[1]]
            return string
        else:
            string += tens[num[0]]
            string += ones[num[1]]
    elif len(num) == 1:
        string += ones[num[0]]

    return string

tk = Tk()
s = Canvas(tk, width = 650, height = 262)
#s.bind("<Button-1>", lambda event: print(event.x, event.y))
s.pack()

img = PhotoImage(file = "chequeImg.gif")
s.create_image(325, 131, image = img)

dollars = s.create_text(25, 160, text = "", font = "Times 18", anchor = W)
cents = s.create_text(540, 160, text = "/100", font = "Times 18", anchor = E)

dollar = Entry(s)
dollar.insert(0, "0.00")

n = datetime.now()
s.create_text(460, 80, text = str(n.day) + "/" + str(n.month) + "/" + str(n.year), anchor = W, font = "Times 15")

s.create_text(85, 135, text = "Jacob Sawatzky", font = "Times 20", anchor = SW)
s.create_window(500, 125, window = dollar, anchor = SW)

#grid(s, 650, 262, 25)

def setValue(event):
    global dollars, cents, dollar
    
    num = dollar.get()
    
    lenN = len(num)-3
    
    numParts = []
    
    start = lenN%3
    if start != 0:
        numParts.append(num[:start])
    
    for i in range(round(lenN/3-0.5)):
        numParts.append(num[3*i+start:3*i+start+3])
    numParts.reverse()
    
    string = ""
    
    for part in range(len(numParts)):
        partStr = getStrNum(numParts[part])
        if partStr != "and ":
            string = getStrNum(numParts[part]) + ext[part] + string
    
    s.itemconfig(dollars, text = string, font = "Times " + str(18-len(numParts)))
    s.itemconfig(cents, text = num[len(num)-2:] + "/100", font = "Times " + str(18-len(numParts)))
    
tk.bind("<Return>", setValue)
    
while True:
    s.update()
    




