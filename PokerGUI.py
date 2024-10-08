import tkinter as tk
from tkinter import simpledialog

class PokerGUI(tk.Tk):
    def __init__(self, human_player, valid_actions):
        super().__init__()
        self.title("Poker Game")
        self.geometry("400x200")
        self.human_player = human_player
        self.valid_actions = valid_actions

        # Create buttons for fold, call, raise
        self.fold_button = tk.Button(self, text="Fold", command=self.fold)
        self.call_button = tk.Button(self, text="Call", command=self.call)
        self.raise_button = tk.Button(self, text="Raise", command=self.raise_action)

        self.fold_button.pack(side="left")
        self.call_button.pack(side="left")
        self.raise_button.pack(side="left")

    def fold(self):
        self.human_player.action = ("fold", 0)
        self.quit()  # This closes the main loop
        self.destroy()  # This destroys the window

    def call(self):
        call_action = next((action for action in self.valid_actions if action["action"] == "call"), 0)
        self.human_player.action = ("call", call_action['amount'])
        self.quit()
        self.destroy()

    def raise_action(self):
        try:
            raise_amount = int(simpledialog.askstring("Raise", "Enter raise amount:"))
            if raise_amount < 0:
                raise ValueError("Invalid raise amount")
            self.human_player.action = ("raise", raise_amount)
        except ValueError:
            # Show a message or default to folding in case of invalid input
            print("Invalid raise input. Defaulting to fold.")
            self.human_player.action = ("fold", 0)
        
        self.quit()
        self.destroy()

