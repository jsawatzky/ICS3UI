'''
Created on Oct 2, 2014

@author: Jacob
'''

from tkinter import *
from utilities import *

from random import *
from threading import Timer

#Boolean for main loop
playing = True

#Constants for reference
WIDTH = 1200
HEIGHT = 800

#Creates the screen
myInterface = Tk()
s = Canvas(myInterface, width=WIDTH, height=HEIGHT, background="#27462c", bd = -2)
s.pack()

#Score
numPlayerWins = 0
numDealerWins = 0
numPushes = 0
numPlayerBlackjacks = 0
numDealerBlackjacks = 0

#Design
s.create_rectangle(314, 625, 818, 725, fill = "#0C210F")
splitRect = s.create_rectangle(-5000, -5000, -5000, -5000, fill = "#0C210F")
s.create_rectangle(382, 75, 886, 175, fill = "#0C210F")

#Pause
paused = False

def unpause():
    global paused
    paused = False

def pause(time):
    global s, paused
    paused = True
    timer = Timer(time, unpause)
    timer.start()
    while paused == True:
        s.update()

#Gets images off a sprite sheet (Source: http://tkinter.unpythonic.net/wiki/PhotoImage)
def subimage(src, l, t, r, b):
    dst = PhotoImage()
    dst.tk.call(dst, 'copy', src, '-from', l, t, r, b, '-to', 0, 0)
    return dst

#Gets the number value of a card
def getValue(type):
    try:
        return int(type)
    except ValueError:
        if type == 'Ace':
            return 1
        elif type == 'Jack':
            return 10
        elif type == 'Queen':
            return 10
        elif type == 'King':
            return 10

#Create Deck
cardSprite = PhotoImage(file = "cards.gif")
cardBack = subimage(cardSprite, 0, 400, 71, 499)
imgFiles = []
cards = []
cardTracker = {}
y = 0
for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
    x = 0
    for type in ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
        x1 = x*72
        y1 = y*100
        imgFile = subimage(cardSprite, x1, y1, x1+71, y1+99)
        imgFiles.append(imgFile)
        img = s.create_image(-5000, -5000, image = imgFiles[imgFiles.index(imgFile)])
        cardTracker[img] = {}
        cardTracker[img]['value'] = getValue(type)
        cardTracker[img]['type'] = type
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
playerSplitHand = []
playerCur = [0, 0]
playerSplitCur = [0, 0]

dealerHand = []
dealerCur = [0, 0]

cont = False
surrenderP = False
standP = False
bustP = False
split = False

#Quit
def finalQuit():
    myInterface.destroy()

def quitFunc():
    global s, money, numPlayerWins, numDealerWins,numPushes, numPlayerBlackjacks, numDealerBlackjacks
    s.delete("all")
    if money < 10:
        s.create_text(600, 400, text = "You can no longer make the minimum bet!", fill = "black", font = "Times 40")
        pause(3)
    else:
        s.create_text(600, 400, text = "Leaving so soon?", fill = "black", font = "Times 60")
        pause(3)
    s.delete("all")
    #Add stats!!!
    s.create_text(600, 50, text = "Stats", fill = "yellow", font = "Times 50")
    if money > 1000:
        s.create_text(600, 150, text = "You gained $" + str(money-1000), fill = "black", font = "Times 30")
    elif money < 1000:
        s.create_text(600, 150, text = "You lost $" + str(1000-money), fill = "black", font = "Times 30")
    else:
        s.create_text(600, 150, text = "You broke even", fill = "black", font = "Times 30")
    s.create_text(600, 250, text = "Your wins: " + str(numPlayerWins), fill = "black", font = "Times 30")
    s.create_text(600, 300, text = "Dealer wins: " + str(numDealerWins), fill = "black", font = "Times 30")
    s.create_text(600, 350, text = "Pushes: " + str(numPushes), fill = "black", font = "Times 30")
    s.create_text(600, 450, text = "Your blackjacks: " + str(numPlayerBlackjacks), fill = "black", font = "Times 30")
    s.create_text(600, 500, text = "Dealer blackjacks: " + str(numDealerBlackjacks), fill = "black", font = "Times 30")
    doneImg = PhotoImage(file = "done.gif")
    doneB = Button(s, image = doneImg, command = finalQuit, bd = -2)
    s.create_window(600, 600, window = doneB)
    while True:
        try:
            s.update()
        except:
            break

#Gets dealer value
def dealerMax(dealerCur):
    num = max(dealerCur)
    if num > 21:
        return min(dealerCur)
    else:
        return num

#Gets all the cards off the screen
def resetCards():
    global s, playerHand, playerSplitHand, dealerHand, cardBacks

    for card in playerHand:
        s.coords(card, -5000, -5000)
    for card in playerSplitHand:
        s.coords(card, -5000, -5000)
    for card in dealerHand:
        s.coords(card, -5000, -5000)
    index = 0
    for card in cardBacks:
        if index != 0:
            s.coords(card, -5000, -5000)
        index += 1

#Draws the card on the screen
def drawCards(showDealer = False):
    global s, playerHand, playerSplitHand, dealerHand, cardBacks, split, dealerTotalNum, dealerCur

    resetCards()

    index = 0
    for card in playerHand:
        s.coords(card, (index*72)+350, 675)
        index += 1

    if split == True:
        index = 0
        for card in playerSplitHand:
            s.coords(card, (index*-72)+850, 575)
            index += 1

    index = 0
    for card in dealerHand:
        if index == 0 and showDealer == False:
            s.coords(cardBacks[9], 850, 125)
        else:
            s.coords(card, (index*-72)+850, 125)
        s.delete(dealerTotalNum)
        if showDealer == False:
            dealerTotalNum = s.create_text(350, 125, text = str(dealerMax(dealerCur)-cardTracker[dealerHand[0]]['value']), fill = "black", font = "Times 15")
        else:
            dealerTotalNum = s.create_text(350, 125, text = str(dealerMax(dealerCur)), fill = "black", font = "Times 15")
        index += 1

#Deals a player another card  
def dealCard(player, showDealer = False, splitHand = False):
    global s, cards, cardTracker, cardIndex, playerHand, playerSplitHand, playerCur, playerSplitCur, dealerHand, dealerCur, split, cardBacks
    global playerTotalNum1, playerTotalNum2, playerTotalNumSplit1, playerTotalNumSplit2, or1, or2, dealerTotalNum
    card = cards[cardIndex]
    if player == "player":
        if splitHand == False:
            playerHand.append(card)
            index = playerHand.index(card)
            xInc = (1100-(index*72+350))/50
            for i in range(0, 50):
                s.coords(cardBacks[1], 1100-(i*xInc), 400+(i*5.5))
                pause(0.0014)
            playerCur[0] += cardTracker[card]['value']
            if cardTracker[card]['value'] == 1:
                playerCur[1] += 11
            else:
                playerCur[1] += cardTracker[card]['value']
            s.delete(playerTotalNum1, playerTotalNum2)
            s.coords(or1, -5000, -5000)
            if playerCur[1] < 22 and playerCur[0] != playerCur[1]:
                playerTotalNum1 = s.create_text(850, 650, text = str(playerCur[1]), fill = "black", font = "Times 15")
                s.coords(or1, 850, 675)
                playerTotalNum2 = s.create_text(850, 700, text = str(playerCur[0]), fill = "black", font = "Times 15")
            else:
                playerTotalNum1 = s.create_text(850, 675, text = str(playerCur[0]), fill = "black", font = "Times 15")
        else:
            playerSplitHand.append(card)
            index = playerSplitHand.index(card)
            xInc = (1100-(index*-72+850))/50
            for i in range(0, 50):
                s.coords(cardBacks[1], 1100-(i*xInc), 400+(i*3.5))
                pause(0.0014)
            playerSplitCur[0] += cardTracker[card]['value']
            if cardTracker[card]['value'] == 1:
                playerSplitCur[1] += 11
            else:
                playerSplitCur[1] += cardTracker[card]['value']
            s.delete(playerTotalNumSplit1, playerTotalNumSplit2)
            s.coords(or2, -5000, -5000)
            if playerSplitCur[1] < 22 and playerSplitCur[0] != playerSplitCur[1]:
                playerTotalNumSplit1 = s.create_text(350, 550, text = str(playerSplitCur[1]), fill = "black", font = "Times 15")
                s.coords(or2, 350, 575)
                playerTotalNumSplit2 = s.create_text(350, 600, text = str(playerSplitCur[0]), fill = "black", font = "Times 15")
            else:
                playerTotalNumSplit1 = s.create_text(350, 575, text = str(playerSplitCur[0]), fill = "black", font = "Times 15")
    elif player == "dealer":
        dealerHand.append(card)
        index = dealerHand.index(card)
        xInc = (1100-(index*-72+850))/50
        for i in range(0, 50):
            s.coords(cardBacks[1], 1100-(i*xInc), 400-(i*5.5))
            pause(0.0014)
        if cardTracker[card]['type'] == 'Ace':
            dealerCur[1] += 11
        else:
            dealerCur[1] += cardTracker[card]['value']
        dealerCur[0] += cardTracker[card]['value']
    drawCards(showDealer)
    cardIndex += 1

#Sets the players bet
def setBetFunc():
    global s, curBet, bet, betW, setBetW
    curBet += bet.get()
    s.coords(betW, -5000, -5000)
    s.coords(setBetW, -5000, -5000)

#Player surrender   
def Surrender():
    global cont, surrenderP
    surrenderP = True
    cont = True

#Player hit   
def Hit():
    global cont
    dealCard("player")
    cont = True

#Player hit when split
def HitSplit():
    global cont, playerSplitHand
    dealCard("player", splitHand = True)
    cont = True

#Player stand
def Stand():
    global cont, standP
    standP = True
    cont = True

#Player double down
def DoubleDown():
    global s, cont, curBet, money, bet, betW, setBetW, betText, split
    money -= curBet
    curBet *= 2
    s.delete(betText)
    if split == False:
        betText = s.create_text(600, 600, text = "$"+str(curBet), fill = "black", font = "Times 12")
    else:
        betText = s.create_text(600, 500, text = "$"+str(curBet), fill = "black", font = "Times 12")
        dealCard("player", splitHand = True)
    dealCard("player")
    standP = True
    cont = None

#Split players hand
def Split():
    global s, cont, cardTraker, money, curBet, playerHand, playerSplitHand, playerCur, playerSplitCur, split, splitRect, betC, betText, curBet, money
    split = True
    otherCard = playerHand.pop(1)
    playerSplitHand.append(otherCard)
    playerCur[0] = cardTracker[otherCard]['value']
    playerSplitCur[0] = cardTracker[otherCard]['value']
    if cardTracker[otherCard]['type'] == 'Ace':
        playerCur[1] = 11
        playerSplitCur[1] = 11
        cont = None
    else:
        playerCur[1] = cardTracker[otherCard]['value']
        playerSplitCur[1] = cardTracker[otherCard]['value']
        cont = True
    money -= curBet
    s.coords(splitRect, 382, 525, 886, 625)
    s.delete(betText)
    s.coords(betC, 600, 475)
    betText = s.create_text(600, 500, text = "$"+str(curBet)+"x2", fill = "black", font = "Times 12")
    for i in range(0, 51):
        s.coords(playerSplitHand[0], 422+(i*8.56), 675-(i*2))
        pause(0.001)
    dealCard("player")
    dealCard("player", splitHand = True)

#Players turn
def playerMove(useSplitHand = False):
    global standP, surrenderP, playerHand, playerCur, playerSplitCur, split, cont, bustP, surrenderW, standW, hitW, hitB, doubleDownW, splitW, money, curBet

    bustP = False
    while standP == False and bustP == False and surrenderP == False:
         
        options = [surrenderW, standW]

        if useSplitHand == False:
            if playerCur[0] < 21:
                options.append(hitW)
                hitB.config(command = Hit)
        else:
            if playerSplitCur[0] < 21:
                options.append(hitW)
                hitB.config(command = HitSplit)
        
        if len(playerHand) == 2:
            if money >= curBet:
                options.append(doubleDownW)
            if cardTracker[playerHand[0]]['type'] == cardTracker[playerHand[1]]['type'] and split == False:
                options.append(splitW)
                
        options.reverse()
        index = 0
        for button in options:
            s.coords(button, 125, 750-(75*index))
            index += 1
                
        while cont == False:
            s.update()

        for button in options:
            s.coords(button, -5000, -5000)
            
        if cont == None:
            cont = False
            break
        cont = False

        if useSplitHand == False:
            if playerCur[0] > 21:
                s.coords(bust, 600, 400)
                bustP = True
                pause(3)
                s.coords(bust, -5000, -5000)
        else:
            if playerSplitCur[0] > 21:
                s.coords(bust, 600, 400)
                bustP = True
                pause(3)
                s.coords(bust, -5000, -5000)

#Components
quitImg = PhotoImage(file = "quit.gif")
quitB = Button(s, image = quitImg, command = quitFunc, bd = -2)
quitW = s.create_window(1090, 60, window = quitB)
                
bet = Scale(s, from_ = 10, to = money, orient = HORIZONTAL, resolution = 10, fg = "white", bg = "#27462c")
betW = s.create_window(-5000, -5000, window = bet)
placeBetImg = PhotoImage(file = "placeBet.gif")
setBet = Button(s, text = "Place bet", image = placeBetImg, command = setBetFunc, bd = -2)
setBetW = s.create_window(-5000, -5000, window = setBet)

surrenderImg = PhotoImage(file = "surrender.gif")
surrenderB = Button(s, text = "Surrender", image = surrenderImg, command = Surrender, bd = -2)
surrenderW = s.create_window(-5000, -5000, window = surrenderB)

hitImg = PhotoImage(file = "hit.gif")
hitB = Button(s, text = "Hit", image = hitImg, command = Hit, bd = -2)
hitW = s.create_window(-5000, -5000, window = hitB)

standImg = PhotoImage(file = "stand.gif")
standB = Button(s, text = "Stand", image = standImg, command = Stand, bd = -2)
standW = s.create_window(-5000, -5000, window = standB)

doubleDownImg = PhotoImage(file = "doubleDown.gif")
doubleDownB = Button(s, text = "Double Down", image = doubleDownImg, command = DoubleDown, bd = -2)
doubleDownW = s.create_window(-5000, -5000, window = doubleDownB)

splitImg = PhotoImage(file = "split.gif")
splitB = Button(s, text = "Split", image = splitImg, command = Split, bd = -2)
splitW = s.create_window(-5000, -5000, window = splitB)

#Text
doubleBlackjack = s.create_text(-5000, -5000, text = "Player and dealer blackjack. Push.", fill = "black", font = "Times 30")
playerBlackjack = s.create_text(-5000, -5000, text = "Blackjack!", fill = "yellow", font = "Times 40")
dealerBlackjack = s.create_text(-5000, -5000, text = "Dealer blackjack", fill = "red", font = "Times 35")
bust = s.create_text(-5000, -5000, text = "Bust", fill = "red", font = "Times 40")
dealerHit = s.create_text(-5000, -5000, text = "Dealer hits", fill = "black", font = "Times 25")
dealerStand = s.create_text(-5000, -5000, text = "Dealer stands", fill = "black", font = "Times 25")
dealerBust = s.create_text(-5000, -5000, text = "Dealer busts", fill = "yellow", font = "Times 25")
playerWins = s.create_text(-5000, -5000, text = "You win!", fill = "yellow", font = "Times 35")
playerWinsSplit1 = s.create_text(-5000, -5000, text = "You win the first hand!", fill = "yellow", font = "Times 30")
playerWinsSplit2 = s.create_text(-5000, -5000, text = "You win the second hand!", fill = "yellow", font = "Times 30")
dealerWins = s.create_text(-5000, -5000, text = "Dealer wins", fill = "red", font = "Times 25")
dealerWinsSplit1 = s.create_text(-5000, -5000, text = "Dealer wins the first hand", fill = "red", font = "Times 25")
dealerWinsSplit2 = s.create_text(-5000, -5000, text = "Dealer wins the second hand", fill = "red", font = "Times 25")
push = s.create_text(-5000, -5000, text = "Push", fill = "black", font = "Times 30")
pushSplit1 = s.create_text(-5000, -5000, text = "Push on first hand", fill = "black", font = "Times 30")
pushSplit2 = s.create_text(-5000, -5000, text = "Push on second hand", fill = "black", font = "Times 30")
betQ = s.create_text(-5000, -5000, text = "Please place a bet", fill = "black", font = "Times 35")
betC = s.create_text(-5000, -5000, text = "Current bet:", fill = "black", font = "Times 15")
betText = None
playerTotalNum1 = None
playerTotalNum2 = None
playerTotalNumSplit1 = s.create_text(-5000, -5000, text = "or", fill = "black", font = "Times 10")#Not sure why i have to do this
playerTotalNumSplit2 = s.create_text(-5000, -5000, text = "or", fill = "black", font = "Times 10")#Not sure why i have to do this
or1 = s.create_text(-5000, -5000, text = "or", fill = "black", font = "Times 10")
or2 = s.create_text(-5000, -5000, text = "or", fill = "black", font = "Times 10")
dealerTotalNum = None

#Backs of cards for dealing
cardBacks = []
for i in range(0, 10):
    cardBacks.append(s.create_image(-5000, -5000, image = cardBack))

#Main Game
def main():
    global s, cards, cardIndex, money, curBet, playerHand, playerSplitHand, playerCur, playerSplitCur, dealerHand, dealerCur, cont, surrenderP, standP, bustP, split
    global bet, betW, setBetW, surrenderW, hitW, standW, doubleDownW, splitW, splitRect
    global doubleBlackjack, playerBlackjack, dealerBlackjack, bust, dealerHit, dealerStand, dealerBust, playerWins, playerWinsSplit1, playerWinsSplit2, dealerWins, dealerWinsSplit1, dealerWinsSplit2, push, pushSplit1, pushSplit2, betQ, betC, betText, playerTotalNum1, playerTotalNum2, playerTotalNumSplit1, playerTotalNumSplit2, or1, or2, dealerTotalNum
    global numPlayerWins, numDealerWins, numPushes, numPlayerBlackjacks, numDealerBlackjacks
    
    shuffle(cards)

    #Gets the players bet
    s.coords(betW, 1000, 750)
    s.coords(setBetW, 1125, 750)
    bet.config(to = money)
    s.coords(betQ, 600, 400)
    while curBet == 0:
        s.update()
    money -= curBet
    s.coords(betQ, -5000, -5000)
    s.coords(betC, 600, 575)
    betText = s.create_text(600, 600, text = "$"+str(curBet), fill = "black", font = "Times 12")
        
    cardIndex = 0

    #Deal the cards
    for i in range(0, 2):
        dealCard("player")
        dealCard("dealer")

    over = False
    pause(1)

    #Check for blackjacks
    if playerCur[1] == 21 and dealerMax(dealerCur) == 21:
        s.coords(doubleBlackjack, 600, 400)
        drawCards(True)
        money += curBet
        numPlayerBlackjacks += 1
        numDealerBlackjacks += 1
        pause(3)
        s.coords(doubleBlackjack, -5000, -5000)
        over = True
    elif playerCur[1] == 21:
        s.coords(playerBlackjack, 600, 400)
        money += curBet*2.5
        numPlayerBlackjacks += 1
        pause(3)
        s.coords(playerBlackjack, -5000, -5000)
        over = True
    elif dealerMax(dealerCur) == 21:
        s.coords(dealerBlackjack, 600, 400)
        drawCards(True)
        numDealerBlackjacks += 1
        pause(3)
        s.coords(dealerBlackjack, -5000, -5000)
        over = True

    if over == False:
        #Players turn
        playerMove()
        if split == True:
            tempBust = bustP
            bustP = False
            tempSurrender = surrenderP
            surrenderP = False
            standP = False
            if cardTracker[playerHand[0]]['type'] != 'Ace':
                pause(1)
                playerMove(True)
                bustSplit = bustP
                bustP = tempBust
                surrenderSplit = surrenderP
                surrenderP = tempSurrender

        #Dealers turn
        if (split == True and (bustP == False or bustSplit == False) and (surrenderP == False or surrenderSplit == False)) or (split == False and bustP == False and surrenderP == False):
            standD = False
            bustD = False
            drawCards(True)
            while standD == False and bustD == False:
                if dealerMax(dealerCur) < 17:
                    dealCard("dealer", True)
                    s.coords(dealerHit, 600, 400)
                    pause(2)
                    s.coords(dealerHit, -5000, -5000)
                elif dealerMax(dealerCur) < 22:
                    standD = True
                    s.coords(dealerStand, 600, 400)
                    pause(2)
                    s.coords(dealerStand, -5000, -5000)
                else:
                    s.coords(dealerBust, 600, 400)
                    bustD = True
                    pause(2)
                    s.coords(dealerBust, -5000, -5000)

        #Determines winner
        winDealer = False
        winPlayer = False
        winDealerSplit1 = False
        winDealerSplit2 = False
        winPlayerSplit1 = False
        winPlayerSplit2 = False
        Push = False
        PushSplit1 = False
        PushSplit2 = False
        if split == False:
            if bustP == True:
                winDealer = True
            elif surrenderP == True:
                money += curBet*0.5
                winDealer = True
            elif bustD == True:
                money += curBet*2
                winPlayer = True
            elif playerCur[1] > 21:
                if playerCur[0] == dealerMax(dealerCur):
                    money += curBet
                    Push = True
                elif playerCur[0] > dealerMax(dealerCur):
                    money += curBet*2
                    winPlayer = True
                elif dealerMax(dealerCur) > playerCur[0]:
                    winDealer = True
            else:
                if playerCur[1] == dealerMax(dealerCur):
                    money += curBet
                    Push = True
                elif playerCur[1] > dealerMax(dealerCur):
                    money += curBet*2
                    winPlayer = True
                elif dealerMax(dealerCur) > playerCur[1]:
                    winDealer = True
        else:
            if bustP == True:
                winDealerSplit1 = True
            elif surrenderP == True:
                money += curBet*0.5
                winDealerSplit1 = True
            elif bustD == True:
                money += curBet*2
                winPlayerSplit1 = True
            elif playerCur[1] > 21:
                if playerCur[0] == dealerMax(dealerCur):
                    money += curBet
                    PushSplit1 = True
                elif playerCur[0] > dealerMax(dealerCur):
                    money += curBet*2
                    winPlayerSplit1 = True
                elif dealerMax(dealerCur) > playerCur[0]:
                    winDealerSplit1 = True
            else:
                if playerCur[1] == dealerMax(dealerCur):
                    money += curBet
                    PushSplit1 = True
                elif playerCur[1] > dealerMax(dealerCur):
                    money += curBet*2
                    winPlayerSplit1 = True
                elif dealerMax(dealerCur) > playerCur[1]:
                    winDealerSplit1 = True
            if bustSplit == True:
                winDealerSplit2 = True
            elif surrenderSplit == True:
                money += curBet*0.5
                winDealerSplit2 = True
            elif bustD == True:
                money += curBet*2
                winPlayerSplit2 = True
            elif playerSplitCur[1] > 21:
                if playerSplitCur[0] == dealerMax(dealerCur):
                    money += curBet
                    PushSplit2 = True
                elif playerSplitCur[0] > dealerMax(dealerCur):
                    money += curBet*2
                    winPlayerSplit2 = True
                elif dealerMax(dealerCur) > playerSplitCur[0]:
                    winDealerSplit2 = True
            else:
                if playerSplitCur[1] == dealerMax(dealerCur):
                    money += curBet
                    PushSplit2 = True
                elif playerSplitCur[1] > dealerMax(dealerCur):
                    money += curBet*2
                    winPlayerSplit2 = True
                elif dealerMax(dealerCur) > playerSplitCur[1]:
                    winDealerSplit2 = True

        if winDealer == True:
            s.coords(dealerWins, 600, 400)
            numDealerWins += 1
            pause(3)
            s.coords(dealerWins, -5000, -5000)
        elif winPlayer == True:
            s.coords(playerWins, 600, 400)
            numPlayerWins += 1
            pause(3)
            s.coords(playerWins, -5000, -5000)
        elif Push == True:
            s.coords(push, 600, 400)
            numPushes += 1
            pause(3)
            s.coords(push, -5000, -5000)
        if winDealerSplit1 == True:
            s.coords(dealerWinsSplit1, 600, 400)
            numDealerWins += 1
            pause(3)
            s.coords(dealerWinsSplit1, -5000, -5000)
        elif winPlayerSplit1 == True:
            s.coords(playerWinsSplit1, 600, 400)
            numPlayerWins += 1
            pause(3)
            s.coords(playerWinsSplit1, -5000, -5000)
        elif PushSplit1 == True:
            s.coords(pushSplit1, 600, 400)
            numPushes += 1
            pause(3)
            s.coords(pushSplit2, -5000, -5000)
        if winDealerSplit2 == True:
            s.coords(dealerWinsSplit2, 600, 400)
            numDealerWins += 1
            pause(3)
            s.coords(dealerWinsSplit2, -5000, -5000)
        elif winPlayerSplit2 == True:
            s.coords(playerWinsSplit2, 600, 400)
            numPlayerWins += 1
            pause(3)
            s.coords(playerWinsSplit2, -5000, -5000)
        elif PushSplit2 == True:
            s.coords(pushSplit2, 600, 400)
            numPushes += 1
            pause(3)
            s.coords(pushSplit2, -5000, -5000)

    #Prepares for the next round
    surrenderP = False
    standP = False
    bustP = False
    split = False
    
    curBet = 0
    s.delete(betText, playerTotalNum1, playerTotalNum2)
    s.coords(playerTotalNumSplit1, -5000, -5000)
    s.coords(playerTotalNumSplit2, -5000, -5000)
    s.delete(dealerTotalNum)
    s.coords(betC, -5000, -5000)
    s.coords(or1, -5000, -5000)
    s.coords(or2, -5000, -5000)
    s.coords(splitRect, -5000, -5000, -5000, -5000)

    resetCards()
    
    playerHand.clear()
    playerSplitHand.clear()
    playerCur = [0, 0]
    playerSplitCur = [0, 0]
    
    dealerHand.clear()
    dealerCur = [0, 0]

def run():
    #More design
    s.coords(cardBacks[0], 1100, 400)
    s.create_text(10, 10, text = "Dealer stands on 17", fill = "white", font = "Times 15", anchor = NW)
    s.create_text(10, 30, text = "Minimum bet: $10", fill = "white", font = "Times 15", anchor = NW)
    s.create_text(600, 30, text = "Dealer", fill = "black", font = "Times 40")
    s.create_text(600, 770, text = "You", fill = "black", font = "Times 40")
    while money >= 10:
        try:
            main()
        except:
            return
    quitFunc()

if __name__ == "__main__":
    run()
