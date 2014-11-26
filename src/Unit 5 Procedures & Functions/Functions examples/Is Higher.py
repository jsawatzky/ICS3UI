def isHigher( card1, card2 ):

    allRanks = ["2","3","4","5","6","7","8","9","10","jack","queen","king","ace"]
    suits = ["clubs","diamonds","hearts","spades"]

    rank1 = card1[0]
    rank2 = card2[0]

    index1 = allRanks.index( rank1 )
    index2 = allRanks.index( rank2 )

    if index1 > index2:
        return True
    elif index1 < index2:
        return False


print(  isHigher( ["jack","diamonds"], ["9","spades"] )    )     
    
    

    
