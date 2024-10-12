from pypokerengine.api.game import setup_config, start_poker
from SmartPlayer import *
from EmotionalPlayer import *
from HumanPlayer import *

print("\n***********************************\n\nStarting the poker game! Good luck!\n\n***********************************\n")

config = setup_config(max_round=100, initial_stack=500, small_blind_amount=10)
config.register_player(name="Andrew", algorithm=HumanPlayer("Andrew"))
config.register_player(name="Daniel", algorithm=SmartPlayer("Daniel"))
config.register_player(name="Anthony", algorithm=EmotionalPlayer("Anthony"))
config.register_player(name="Evan", algorithm=SmartPlayer("Evan"))
game_result = start_poker(config, verbose=1)