class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def printCard(self):
        if self.value < 11:
            print('{} of {}'.format(self.value, self.suit))
        elif self.value == 11:
            print('J of {}'.format(self.suit))
        elif self.value == 12:
            print('Q of {}'.format(self.suit))
        elif self.value == 13:
            print('K of {}'.format(self.suit))
        elif self.value == 14:
            print('A of {}'.format(self.suit))