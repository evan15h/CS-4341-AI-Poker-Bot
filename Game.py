from pypokerengine.api.game import setup_config, start_poker
from CustomAI import CustomAI
from HumanPlayer import HumanPlayer

# Setting up the game configuration with a human and three AI bots
def setup_poker_game():
    config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=10)
    
    # Register human player
    config.register_player("Human", HumanPlayer())
    
    # Register AI players
    config.register_player("AI_Bot_1", CustomAI("AI_Bot_1"))
    config.register_player("AI_Bot_2", CustomAI("AI_Bot_2"))
    config.register_player("AI_Bot_3", CustomAI("AI_Bot_3"))

    return config

def start_game():
    config = setup_poker_game()
    
    # Start the poker game using the pypokergame engine
    game_result = start_poker(config, verbose=1)
    print(game_result)  # Display final results

if __name__ == "__main__":
    start_game()