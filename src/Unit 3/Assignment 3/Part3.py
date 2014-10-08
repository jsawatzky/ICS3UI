'''
Created on Oct 2, 2014

@author: Jacob
'''

from tkinter import *
from utilities import *

from random import *
from threading import Thread

#Boolean for update loops
playing = True

#Constants for reference
WIDTH = 800
HEIGHT = 800

#Creates the screen
myInterface = Tk()
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="#27462c")
s.pack()

#Gets images off a sprite sheet (Source: http://tkinter.unpythonic.net/wiki/PhotoImage)
def subimage(src, l, t, r, b):
    dst = PhotoImage()
    dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
    return dst


#Create Deck
cardSprite = PhotoImage(file = "cards.gif")
cardBack = subimage(cardSprite, 0, 400, 71, 499)
cards = []
cardTracker = {}
y = 0
for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
    x = 0
    for type in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]:
        x1 = x*72
        y1 = y*100
        img = s.create_image(-5000, -5000, image = subimage(cardSprite, x1, y1, x1+71, y1+99))
        cardTracker[img] = {}
        cardTracker[img]['holder'] = "deck"
        cardTracker[img]['value'] = type
        cardTracker[img]['suit'] = suit
        cards.append(img)
        x += 1
    y += 1

#Variables
cardIndex = 0

money = 1000
curBet = 0
curInsurance = 0

playerHand = []
playerCur = [0, 0]

dealerHand = []
dealerCur = 0

#Functions
def setBetFunc():
    global s, curBet, bet, betW, setBetW
    curBet = bet.get()
    s.coords(betW, -5000, -5000)
    s.coords(setBetW, -5000, -5000)
    
def dealCard(player):
    global cards, cardTracker, cardIndex, playerHand, playerCur, dealerHand, dealerCur
    card = cards[cardIndex]
    if player == "player":
        playerHand.append(card)
        cardTracker[card]['holder'] = "player"
        playerCur[0] += cardTracker[card]['value']
        if cardTracker[card]['value'] == 1:
            playerCur[1] += 11
        else:
            playerCur[1] += cardTracker[card]['value']
    elif player == "dealer":
        dealerHand.append(card)
        cardTracker[card]['holder'] = "dealer"
        if cardTracker[card]['value'] == 1:
            if dealerCur > 10:
                dealerCur += 1
            else:
                dealerCur += 11

#Components
bet = Scale(s, from_ = 10, to = money, orient = HORIZONTAL, resolution = 10)
betW = s.create_window(-5000, -5000, window = bet)
setBet = Button(s, text = "Enter", command = setBetFunc) #Add an image as the button
setBetW = s.create_window(-5000, -5000, window = setBet)

def main():
    global s, cards, cardIndex, money, curBet, curInsurance, playerHand, playerCur, dealerHand, dealerCur
    global betW, setBetW
    
    shuffle(cards)
    
    s.coords(betW, 650, 750)
    s.coords(setBetW, 750, 750)
    while curBet == 0:
        print("Waiting")
        
    cardIndex = 0
    
    for i in range(0, 2):
        dealCard("player")
        dealCard("dealer")
        
    if max(playerCur[0], playerCur[1]) == 21 and dealerCur == 21:
        ##Push
        print("Push")
    elif playerCur == 21:
        ##Player Blackjack
        print("Player Blackjack")
    elif dealerCur == 21:
        ##Dealer Blackjack
        print("Dealer Blackjack")
        
    #Player move
    stand = False
    bust = False
    
    index = 0
    for card in playerHand:
        print("Card drawn")
        s.coords(card, index*72, 0)
        s.update()
        index += 1
    
#     while stand == False and bust == False:
#         
#         options = []
#         
#         
#         
#         if playerCur[0] > 21:
#             print("bust")
        
    
    curBet = 0
    curInsurance = 0
    
    playerHand.clear()
    playerCur[0] = 0
    playerCur[1] = 0
    
    dealerHand.clear()
    dealerCur = 0
        
class MainThread(Thread):
    
    def run(self):
        global playing
        while playing == True:
            main()
            
mainThread = MainThread()
mainThread.start()

while True:
    s.update()