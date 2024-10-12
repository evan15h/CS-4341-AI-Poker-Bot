from pypokerengine.players import BasePokerPlayer

class HumanPlayer(BasePokerPlayer):

    def __init__(self, name):
        self.name = name

    def declare_action(self, valid_actions, hole_card, game_state):
       
        # valid_actions => [fold_action_info, call_action_info, raise_action_info]
        call_action_info = valid_actions[1]
        raise_action_info = valid_actions[2]

        amount = 0
        while(True):
            action = input("Enter your action (Must match one of the following: 'raise', 'call', 'fold'): ")
            print("\n")
            if action == 'raise' or action == 'call' or action == 'fold':
                break
   
        if action == 'raise':
            while(True):  
                min_raise = raise_action_info["amount"]["min"]
                max_raise = raise_action_info["amount"]["max"]
                amount = input(f"How much would you like to raise (Must be an integer between {min_raise} and {max_raise}) ")
                print("\n")
                if amount.isdigit():
                    amount = int(amount)
                    for player in game_state['seats']:
                        if player['name'] == self.name:
                            stack = player['stack']
                            print(f"This is your stack: {stack}")
                            if amount <= max_raise and amount >= min_raise:
                                return action, amount
        elif action == 'call':
            amount = call_action_info["amount"]
            return action, amount
        if action == 'fold':
            return action,amount

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        print(f"Your hole cards for the next hand are: {hole_card}\n\n")

    def receive_street_start_message(self, street, game_state):
        pass

    def receive_game_update_message(self, action, game_state):
        pass

    def receive_round_result_message(self, winners, hand_info, game_state):
        pass