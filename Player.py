from Card import *
from Emotion import *

#Intelligent agent class
class Player:

    def __init__(self, name, money = 0):
        self.cards = []
        self.name = name
        self.money = money
        self.emotion = Emotion()

    def addCard(self, card):
        self.cards.append(card)

    def printCards(self):
        for card in self.cards:
            card.printCard()
        print('\n')

    def makeDecision(self):
        
        # Base decision logic
        # base_decision =
        
        # Final decision, use emotion.adjust_decision
        # final_decision =

        pass

    def updateEmotion(self, result):
        # Update emotional state based on round's outcome
        self.emotion.update_emotion(result)