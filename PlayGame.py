from pypokerengine.api.game import setup_config, start_poker
from SmartPlayer import *
from EmotionalPlayer import *
from HumanPlayer import *

print("\n***********************************\n\nStarting the poker game! Good luck!\n\n***********************************\n")

# Set up game parameters
config = setup_config(max_round=100, initial_stack=500, small_blind_amount=10)

# Human players
config.register_player(name="Human", algorithm=HumanPlayer("Human"))

# Smart players
config.register_player(name="Smart 1", algorithm=SmartPlayer("Smart 1"))
config.register_player(name="Smart 2", algorithm=SmartPlayer("Smart 2"))

# Emotional players
config.register_player(name="Emotional 1", algorithm=EmotionalPlayer("Emotional 1"))

# Begin game
game_result = start_poker(config, verbose=1)
