from pypokerengine.api.game import setup_config, start_poker
from SmartPlayer import *
from EmotionalPlayer import *
from HumanPlayer import *

print("\n***********************************\n\nStarting the poker game! Good luck!\n\n***********************************\n")

config = setup_config(max_round=1, initial_stack=500, small_blind_amount=10)
config.register_player(name="Jake", algorithm=SmartPlayer("Jake"))
config.register_player(name="Evan", algorithm=HumanPlayer("Evan"))
config.register_player(name="Nate", algorithm=EmotionalPlayer("Nate"))
config.register_player(name="Anthony", algorithm=EmotionalPlayer("Anthony"))
game_result = start_poker(config, verbose=1)