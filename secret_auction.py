'''
Date: 09-11-2023
Author: Sumanth S Kumar
Summary: This program creates a silent auction where many bidders
can bid for a particular item. The bidding is done on a single computer
where bidders take turn to input their bids.
As the auction is silent, bidders cannot access each other's bids.
'''

import os

bids = {}
repeat = True

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def add_bid(bidder, bid):
    bids[bidder] = bid
    return bids
def key_maxvalue():
    k = list(bids.keys())
    v = list(bids.values())
    max_k = k[v.index(max(v))]
    return max_k


print('Welcome to the secret auction program')
while repeat == True:
    cls()
    bidder = input('What is your name?: ')
    bid = int(input('What is your bid? $'))
    add_bid(bidder, bid)
    more_bidders = input("Are there more bidders? type 'yes' or 'no'\n")
    if more_bidders == 'no':
        repeat = False


else:
    print(f"{key_maxvalue()} wins with a bid of {bids[key_maxvalue()]}")
