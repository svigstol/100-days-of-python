# 100 Days of Python
# Day 9 - Silent Auction
# Enter name/bid from multiple users. When finished, display highest bid.
# Sarah Vigstol
# 5/30/21

import click
import userexp

bids = {}
displayWinner = False

print(userexp.logo)
print(userexp.art)

while displayWinner == False:
    name = input("Please enter your name: ")
    bid = int(input(f"Hello, {name}. Enter your bid now: $"))
    bids[name] = bid

    moreBids = input("Any other takers? Type 'yes or 'no.' ").lower()
    if moreBids == "no":
        winner = max(bids, key=bids.get)
        winningBid = "{:.2f}".format(bids[winner])
        print(f"The winner is {winner} with a bid of ${winningBid}.")
        displayWinner = True
    else:
        click.clear()
