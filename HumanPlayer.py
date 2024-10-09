from pypokerengine.players import BasePokerPlayer
from tkinter import simpledialog, Tk

class HumanPlayer(BasePokerPlayer):

    def __init__(self):
        self.action = None

    def declare_action(self, valid_actions, hole_card, game_state):
        # gui = PokerGUI(self, valid_actions)
        # gui.mainloop()  # Wait for the GUI to close

        amount = 0
        while(True):
            action = input("Enter your action (Must match one of the following: 'raise', 'call', 'fold'): ")
            if action == 'raise' or action == 'call' or action == 'fold':
                break
    
        if action == 'raise':
            while(True):   
                amount = input("How much would you like to raise (Must be an integer)? ")
                if amount.isdigit():
                    amount = int(amount)
                    break
        if action == 'call':
            pass
        if action == 'fold':
            pass


        self.action = action, amount
        return self.action



    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        print(f"Round {round_count} started. Hole cards: {hole_card}")

    def receive_street_start_message(self, street, game_state):
        pass

    def receive_game_update_message(self, action, game_state):
        pass

    def receive_round_result_message(self, winners, hand_info, game_state):
        print("\nRound Result:")
        for winner in winners:
            print(f"Winner: {winner['name']} with stack: {winner['stack']}")
        print(f"Hand Info: {hand_info}")
        print(f"Pot Size: {game_state['pot']['main']['amount']}")
        # Show player stacks for each player
        for player in game_state['seats']:
            print(f"Player {player['name']} has stack: {player['stack']}")
        pass

