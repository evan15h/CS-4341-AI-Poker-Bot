from pypokerengine.players import BasePokerPlayer
import tkinter as tk
from pypokerengine.api.game import setup_config, start_poker
from CustomAI import CustomAI
#from HumanPlayer import HumanPlayer

# HumanPlayer.py
class HumanPlayer(BasePokerPlayer):

    def __init__(self):
        self.action = None

    def declare_action(self, valid_actions, hole_card, game_state):
        #gui = PokerGUI(self, valid_actions)
        #gui.mainloop()  # Wait for the GUI to close
        wait_for_response()
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


window = tk.Tk()
window.title('Emotional Poker Bots')
window.minsize(1500, 1000)

response = False

# Need some signal to wait for button press
def wait_for_response():
    global response

    while(True):
        if response == True:
            response = False
            break
    
    return

# Callback function for calling
def call():
    call_action = next((action for action in human.valid_actions if action["action"] == "call"), 0)
    human_player.action = ("call", call_action['amount'])
    response = True

# Callback function for folding
def fold():
    human_player.action = ("fold", 0)
    response = True

# Callback function for raising
def bet():
    response = True

# Callback function for checking
def check():
    response = True

# Checks if the raise amount is valid
def valid_raise():
    pass


# Assuming it instantly updates and brings to the human players turn, would not need to disable these
check = tk.Button(window, text='check', command = check)
check.place(x=100, y=900)

call = tk.Button(window, text='call', command = call)
call.place(x=200, y=900)

fold = tk.Button(window, text='fold', command = fold)
fold.place(x=300, y=900)

# raise is already a keyword so used bet
bet = tk.Button(window, text='raise', command = bet)
bet.place(x=400, y=900)

bet_amount = tk.Entry(window, text='enter raise amount', validatecommand=valid_raise)
bet_amount.place(x=500, y=900)

human_player = tk.Label(window, text='Human Player')
human_player.place(x = 750, y = 800)

human_chips = tk.Label(window, text='Chips: 0')
human_chips.place(x=750, y=750)

AI1_player = tk.Label(window, text='AI 1')
AI1_player.place(x = 100, y= 500)

AI1_chips = tk.Label(window, text='Chips: 0')
AI1_chips.place(x=100, y= 600)

AI2_player = tk.Label(window, text='AI 2')
AI2_player.place(x = 750, y= 100)

AI2_chips = tk.Label(window, text='Chips: 0')
AI2_chips.place(x=750, y= 200)

AI3_player = tk.Label(window, text='AI 3')
AI3_player.place(x = 1300, y= 500)

AI3_chips = tk.Label(window, text='Chips: 0')
AI3_chips.place(x=1300, y= 600)

pot = tk.Label(window, text='Pot: 0')
pot.place(x=750, y= 600)

canvas = tk.Canvas(window, width= 200, height = 200, borderwidth=0, highlightthickness=0)
canvas.place(x = 650, y= 350)
card = canvas.create_rectangle(10, 10, 20, 60)

#Start poker stuff here
config = setup_config(max_round=100, initial_stack=1000, small_blind_amount=10)
    
# Register human player
human = HumanPlayer()
config.register_player(name="Human", algorithm=human)
    
# Register AI players
config.register_player(name="AI_Bot_1", algorithm=CustomAI())
config.register_player(name="AI_Bot_2", algorithm=CustomAI())
config.register_player(name="AI_Bot_3", algorithm=CustomAI())


log = tk.Label(window, text='log')
log.place(x=750, y=300)
# Start the poker game using the pypokergame engine
game_result = start_poker(config, verbose=1)
log.config(text=game_result)
#print(game_result)  # Display final results

window.mainloop()
