from Deck import *
from Player import *

#UI and agent will draw from this
#Deals cards and keeps track of pots and stuff

class Game:

    def __init__(self):
        self.players = []
        self.playersInHand = []
        self.bet = 0
        self.pot = 0
        self.whoseTurn = None
        self.dealer = None
        self.communityCards = []
        self.deck = Deck()
        self.deck.shuffle()
    
    #Adds players to the game
    def addPlayers(self):
        p1 = Player('p1')
        p2 = Player('p2')
        p3 = Player('p3')
        p4 = Player('p4')
        self.players.append(p1)
        self.players.append(p2)
        self.players.append(p3)
        self.players.append(p4)

    #Deal cards to players
    def deal(self):

        for i in range(2):
            for player in self.players:
                player.addCard(self.deck.getTopCard())
                self.playersInHand.append(player)

    def flop(self):
        #Burn
        self.deck.getTopCard()

        #Add 3 cards
        for i in range(3):
            self.communityCards.append(self.deck.getTopCard())
    
    def turn(self):
        #Burn
        self.deck.getTopCard()

        #Add 1 card
        self.communityCards.append(self.deck.getTopCard())

    def river(self):
        #Burn
        self.deck.getTopCard()

        #Add 1 card
        self.communityCards.append(self.deck.getTopCard())

    def playerAction(self, player, action, amount = 0):
        
        if action == 'check':
            pass

        elif action == 'call':
            player.chips -= self.bet
            self.pot += self.bet

        elif action == 'bet':
            self.pot += amount
            self.bet = amount

        elif action == 'fold':
            self.playersInHand.remove(player)

        #Update whose turn it is


def main():
    game = Game()
    game.addPlayers()
    game.deal()
    game.flop()
    game.turn()
    game.river()

    for player in game.players:
        player.printCards()
    
    for card in game.communityCards:
        card.printCard()

if __name__ == "__main__":
    main()
