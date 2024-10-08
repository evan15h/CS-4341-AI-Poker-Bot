from pypokerengine.players import BasePokerPlayer
from tkinter import simpledialog, Tk
from PokerGUI import PokerGUI

class HumanPlayer(BasePokerPlayer):

    def __init__(self):
        self.action = None

    def declare_action(self, valid_actions, hole_card, game_state):
        gui = PokerGUI(self, valid_actions)
        gui.mainloop()  # Wait for the GUI to close
        return self.action


    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, game_state):
        pass

    def receive_game_update_message(self, action, game_state):
        pass

    def receive_round_result_message(self, winners, hand_info, game_state):
        pass
