# 100 Days of Python
# Day 9 - Silent Auction
# Enter name/bid from multiple users. When finished, display highest bid.
# Sarah Vigstol
# 5/30/21

import click
import userexp

def silentAuction():
    print(userexp.logo)
    print(userexp.art)

    bids = {}
    displayWinner = False

    while displayWinner == False:
        name = input("Please enter your name: ")
        bid = float(input(f"Hello, {name}. Enter your bid now: $"))
        bids[name] = bid

        moreBids = input("Any other takers? Type 'yes or 'no.' ").lower()
        if moreBids == "yes":
            click.clear()
        elif moreBids == "no":
            winner = max(bids, key=bids.get)
            winningBid = "{:.2f}".format(bids[winner])
            print(f"The winner is {winner} with a bid of ${winningBid}.\n")

            gameCheck = True
            while gameCheck == True:
                goAgain = input("Start a new auction? Type 'yes' or 'no.' ").lower()
                if goAgain == "yes":
                    # multiRound == False
                    click.clear()
                    silentAuction()
                elif goAgain == "no":
                    print("Goodbye!")
                    quit()
                else:
                    print("Invalid input. Please try again.\n")

            displayWinner = True

        else:
            print("Invalid input. Please try again.\n")

silentAuction()
