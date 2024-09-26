from Card import *

#Intelligent agent class
class Player:

    def __init__(self, name, money = 0):
        self.cards = []
        self.name = name
        self.money = money

    def addCard(self, card):
        self.cards.append(card)

    def printCards(self):
        for card in self.cards:
            card.printCard()
        print('\n')

    def makeDecision(self):
        pass