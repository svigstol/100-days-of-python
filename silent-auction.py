# 100 Days of Python
# Day 9 - Silent Auction
# Enter name/bid from multiple users. When finished, display highest bid.
# Sarah Vigstol
# 5/30/21

bids = {}
userName = input("Who is bidding?\n> ")
userBid = input(f"Hello, {userName}. What would you like to bid?\n> ")
bids[userName] = userBid

print(bids)
