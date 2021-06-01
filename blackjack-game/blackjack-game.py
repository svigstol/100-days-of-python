# 100 Days of Python
# Day 11 - Blackjack Game
# Beat the dealer's hand without going over 21.
# Sarah Vigstol
# 5/31/21

deck = [
    {
        "Ace of Hearts": 11,
        "Two of Hearts": 2,
        "Three of Hearts": 3,
        "Four of Hearts": 4,
        "Five of Hearts": 5,
        "Six of Hearts": 6,
        "Seven of Hearts": 7,
        "Eight of Hearts": 8,
        "Nine of Hearts": 9,
        "Ten of Hearts": 10,
        "Jack of Hearts": 10,
        "Queen of Hearts": 10,
        "King of Hearts": 10
    },
    {
        "Ace of Diamonds": 11,
        "Two of Diamonds": 2,
        "Three of Diamonds": 3,
        "Four of Diamonds": 4,
        "Five of Diamonds": 5,
        "Six of Diamonds": 6,
        "Seven of Diamonds": 7,
        "Eight of Diamonds": 8,
        "Nine of Diamonds": 9,
        "Ten of Diamonds": 10,
        "Jack of Diamonds": 10,
        "Queen of Diamonds": 10,
        "King of Diamonds": 10
    },
    {
        "Ace of Spades": 11,
        "Two of Spades": 2,
        "Three of Spades": 3,
        "Four of Spades": 4,
        "Five of Spades": 5,
        "Six of Spades": 6,
        "Seven of Spades": 7,
        "Eight of Spades": 8,
        "Nine of Spades": 9,
        "Ten of Spades": 10,
        "Jack of Spades": 10,
        "Queen of Spades": 10,
        "King of Spades": 10
    },
    {
        "Ace of Clubs": 11,
        "Two of Clubs": 2,
        "Three of Clubs": 3,
        "Four of Clubs": 4,
        "Five of Clubs": 5,
        "Six of Clubs": 6,
        "Seven of Clubs": 7,
        "Eight of Clubs": 8,
        "Nine of Clubs": 9,
        "Ten of Clubs": 10,
        "Jack of Clubs": 10,
        "Queen of Clubs": 10,
        "King of Clubs": 10
    }
]

import random

gameSet = False

playerHand = {}
dealerHand = {}

def drawCard():
    suit = random.choice(deck)
    cardList = list(suit.items())
    card = random.choice(cardList)
    return(card)

playerCard = drawCard()
dealerCard = drawCard()

print(f"You drew: {playerCard")
print(f"Dealer drew: {dealerCard}")

while gameSet == False:
    drawNew = input("Hit? Y/N: ").lower()

    if drawNew == "y":
        playerCardTwo = drawCard()
        dealerCardTwo = drawCard()
        # playerCards = playerCardOne + playerCardTwo

        print(f"You drew: {playerCardTwo}")
        print(f"Dealer drew: {dealerCardTwo}")

    elif drawNew == "n":
        dealerCardTwo = drawCard()
        print(f"Computer drew: {dealerCardTwo}")
    else:
        print("Invalid input. Try again.")
