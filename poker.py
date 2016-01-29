# -*- coding: utf-8 -*-
import random

#kortstokk er delt i 14 verdier og 4 sorter, 10 har en egen verdi så den ikke deles opp og blir 2 kort 0 og 1
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

#dette er handen hver spiller er utdelt
def poker(hands):
    h = deal(hands)
    n = 1
    while n <= len(h):
        print "Hand", n, ":", h[n-1], "\n" 
        n = n + 1


# Denne funksjonen deler til alle spillere "numhands", med n kort i til hver hand. Bruker random til å dele ut
def deal(numhands, n=5, deck=mydeck):
    
    random.shuffle(deck)
    shuffeleddeck = [deck[n*i:n*(i+1)] for i in range(numhands)]
    return shuffeleddeck


print poker(5) #fem spillere i dette eksempelet