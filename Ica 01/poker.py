# -*- coding: utf-8 -*-
import random
import re

#kortstokk er delt i 13 verdier og 4 sorter, 10 har en egen verdi så den ikke deles opp og blir 2 kort 0 og 1.
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

#dette er handen hver spiller er utdelt
def poker(hands):
    h = deal(hands)
    n = 1
    while n <= len(h):
        print "Hand", n, ":", h[n-1], "\n" 
        n = n + 1
    
    #funksjonen er ikke i bruk enda
    #print "\nWinner hand:"
    #return winner(hand_rank)

def card_ranks(hand):
    ranks = ["--23456789TJQKA".index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks


#def kind(n, ranks):
def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
        
#def flush():
def flush(hand):
    flushsort = [s for r, s in hand]
    return len(set(flushsort)) == 1


#def straight():
def straight(ranks):
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5


#def pair():
def two_pair(ranks):
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


# Denne funksjonen deler til alle spillere "numhands", med n kort i til hver hand. Bruker random til å dele ut
def deal(numhands, n=5, deck=mydeck):
    
    random.shuffle(deck)
    shuffeleddeck = [deck[n*i:n*(i+1)] for i in range(numhands)]
    return shuffeleddeck


#hvilken verdi hver hand har
def hand_rank(hand):
    ranks = card_ranks(hand)
    
    if flush(hand):
        return (5, max(ranks))

    elif straight(ranks):
        return (4, max(ranks))
    
    elif two_pair(ranks):
        return (2, two_pair(ranks), kind(1, ranks))

#denne skal returnere hvilken hand som vinner, er ikke ferdig
#def winner(hand_rank):
    

print poker(5) #fem spillere i dette eksempelet
