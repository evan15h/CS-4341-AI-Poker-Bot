from Card import *
import random

class Deck:

    def __init__(self):
        cards = []
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        for suit in suits:
            for value in range(13):
                cards.append(Card(value + 2, suit))
        
        self.cards = cards

    def printDeck(self):
        for card in self.cards:
            card.printCard()

    def shuffle(self):
        random.shuffle(self.cards)

    def getTopCard(self):
        return self.cards.pop()


#deck = Deck()
#deck.shuffle()
#deck.printDeck()