'''
Created on Sep 29, 2014

@author: Jacob
'''
import subprocess

again = True
while again == True: 
    
    ##Asks which part the user wants to do
    print("Assignment 2:")
    print("Part 1: Cash counting")
    print("Part 2: String art")
    print("Part 3: Animation")
    part = input("Which part would you like to do? (1/2/3): ")
    while part != "1" and part != "2" and part != "3":
        part = input("Invalid! Must be 1, 2 or 3! Please try again: ")
        
    ##Main Code
    if part == "1":
        subprocess.call("Part1.py", shell=True)
    elif part == "2":
        pass
    else:
        pass
    
        
    ##Asks if user wants do do another one
    again = input("Would you like to do another? (y/n): ")
    while again != "y" and again != "n":
        again = input("Invalid! Please enter a y or an n: ")
    if again == "y":
        again = True
    else:
        again = False