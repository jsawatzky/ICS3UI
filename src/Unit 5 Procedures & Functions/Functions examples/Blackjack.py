from math import *

def getValue( card ):
    rank = card[0]

    if rank == "ace":
        return 11

    elif rank == "king" or rank == "queen" or rank == "jack":
        return 10

    else:
        return int(rank)


def makeDeck():
    deck = []
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = ["clubs","diamonds","hearts","spades"]

    for r in ranks:
        for s in suits:
            newCard = [r,s]
            deck.append( newCard )

    return deck


def printDeck( deck ):
    for i in range(0,13):
        print( deck[4*i], deck[4*i+1], deck[4*i+2], deck[4*i+3])


def f( x ):
    return x**2


myDeck = makeDeck()

printDeck(myDeck)
    

        
