###############################################################################
#TITLE:  Test cases.py
#DESCRIPTION:  Tests the numberSpeller package on a range of numbers 
#PROGRAMMERS:  J. Schattman
#LAST MODIFIED:  11/26/2013
###############################################################################

from numberSpellingTools import *


#TEST CASES
N = "7"
print (N + " is spelled " + spellAnyNumber( N ))


N = "47"
print (N + " is spelled " + spellAnyNumber( N ))


N = "207"
print (N + " is spelled " + spellAnyNumber( N ))


N = "257"
print (N + " is spelled " + spellAnyNumber( N ))


N = "300"
print (N + " is spelled " + spellAnyNumber( N ))


N = "3500"
print (N + " is spelled " + spellAnyNumber( N ))
