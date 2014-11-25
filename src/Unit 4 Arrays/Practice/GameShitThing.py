'''
Created on Oct 30, 2014

@author: Jacob Sawatzky
'''
players = ["Jacob", "Omar", "Simon", "Frank", "Joe", "Bob", "Cody", "Caleb"]
phrase = ["You", "are", "not", "it"]

playerIndex = 0

while len(players) > 1:
    for word in phrase:
        if word == "it":
            print(players[playerIndex] + " is out")
            players.remove(players[playerIndex])
            print("Players left: " + str(players))
        else:
            print(word + " is " + players[playerIndex])
            playerIndex += 1
            
        if playerIndex > len(players)-1: playerIndex = 0
            
print(players[0] + " wins")