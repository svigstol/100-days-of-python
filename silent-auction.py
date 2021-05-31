# 100 Days of Python
# Day 9 - Silent Auction
# Enter name/bid from multiple users. When finished, display highest bid.
# Sarah Vigstol
# 5/30/21

import click

bids = {}
displayWinner = False

# def gatherInput(userName, userBid):


while displayWinner == False:
    name = input("Please enter your name: ")
    bid = int(input(f"Hello, {name}. Enter your bid now: $"))
    bids[name] = bid

    moreBids = input("Any other takers? Type 'yes or 'no.' ").lower()
    if moreBids == "no":
        displayWinner = True
    else:
        click.clear()


# gatherInput(userName=name, userBid=bid)
print(bids)
