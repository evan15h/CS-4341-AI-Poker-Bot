import tkinter as tk

window = tk.Tk()
window.title('Emotional Poker Bots')
window.minsize(1500, 1000)

# Callback function for calling
def call():
    pass

# Callback function for folding
def fold():
    pass

# Callback function for raising
def bet():
    pass

# Callback function for checking
def check():
    pass

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

window.mainloop()