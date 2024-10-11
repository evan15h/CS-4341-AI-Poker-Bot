from pypokerengine.players import BasePokerPlayer
from tkinter import simpledialog, Tk

class HumanPlayer(BasePokerPlayer):

    def __init__(self):
        self.action = None

    def declare_action(self, valid_actions, hole_card, game_state):
        
        # valid_actions => [raise_action_info, call_action_info, fold_action_info]
        call_action_info = valid_actions[1]

        amount = 0
        while(True):
            action = input("Enter your action (Must match one of the following: 'raise', 'call', 'fold'): ")
            if action == 'raise' or action == 'call' or action == 'fold':
                break
    
        if action == 'raise':
            flag = 0
            while(flag == 0):   
                amount = input("How much would you like to raise (Must be an integer)? ")
                if amount.isdigit():
                    amount = int(amount)
                    for player in game_state['seats']:
                        if player['name'] == 'Human':
                            stack = player['stack']
                            print(f"This is the stack: {stack}")
                            if amount <= stack and amount > 0:
                                flag = 1
                                break
            # action,amount = raise_action_info["action"], raise_action_info["amount"]
        if action == 'call':
            amount = call_action_info["amount"]
            pass
        if action == 'fold':
            pass

        self.action = action, amount
        return self.action



    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        print(f"Hand {round_count} started. Hole cards: {hole_card}")

    def receive_street_start_message(self, street, game_state):
        pass

    def receive_game_update_message(self, action, game_state):
        pass

    def receive_round_result_message(self, winners, hand_info, game_state):
        print("\nHand Result:")
        for winner in winners:
            print(f"Winner: {winner['name']} with stack: {winner['stack']}")
        print(f"Hand Info: {hand_info}")
        print(f"Pot Size: {game_state['pot']['main']['amount']}")
        # Show player stacks for each player
        for player in game_state['seats']:
            print(f"Player {player['name']} has stack: {player['stack']}")
        pass

