from Deck import *
from Player import *

#UI and agent will draw from this
#Deals cards and keeps track of pots and stuff

p1 = Player('p1')
p2 = Player('p1')
p3 = Player('p1')
p4 = Player('p1')

def deal(p1, p2, p3, p4):

    deck = Deck()
    deck.shuffle()

    p1.addCard(deck.getTopCard())
    p2.addCard(deck.getTopCard())
    p3.addCard(deck.getTopCard())
    p4.addCard(deck.getTopCard())
    p1.addCard(deck.getTopCard())
    p2.addCard(deck.getTopCard())
    p3.addCard(deck.getTopCard())
    p4.addCard(deck.getTopCard())

    return deck

deck = deal(p1, p2, p3, p4)

p1.printCards()
p2.printCards()
p3.printCards()
p4.printCards()

print(len(deck.cards))
