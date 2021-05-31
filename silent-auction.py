# 100 Days of Python
# Day 9 - Silent Auction
# Enter name/bid from multiple users. When finished, display highest bid.
# Sarah Vigstol
# 5/30/21

bids = {}
displayWinner = False

name = input("Please enter your name: ")
bid = int(input(f"Hello, {name}. Enter your bid now: $"))

def gatherInput(userName, userBid):
    bids[userName] = "{:.2f}".format(userBid)

#    moreBids = input("""
#    Would any one else like to bid?\n
#    Enter 'yes' or 'no. '
#    """).lower()
#    if moreBids == "no":
#        displayWinner = True

gatherInput(userName=name, userBid=bid)
print(bids)
