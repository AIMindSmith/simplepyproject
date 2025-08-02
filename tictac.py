## buiding a tic tac game
# play  with computer
#let's play it with computer
#how to play
"""
you can play tic tac toe with computer.
the game is played on a 3x3 grid.

the first player is "X" and the second player is "O".
the players take turns placing their marks in the empty squares.

the goal of the game is to get three of your marks in a row, column, or diagonal.
if all squares are filled and no player has three in a row, the game is a tie.  
caution: human builds the computer, not the computer building the human.
let's play!
"""


import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.game_mode = None
        self.setup_mode_selection()

    def setup_mode_selection(self):
        self.mode_frame = tk.Frame(self.root)
        self.mode_frame.pack(pady=20)
        
        tk.Label(self.mode_frame, text="Choose Game Mode", font=("Arial", 20)).pack()
        
        tk.Button(self.mode_frame, text="Play vs Computer", font=("Arial", 16),
                 command=lambda: self.start_game("computer")).pack(pady=10)
        
        tk.Button(self.mode_frame, text="Play vs Friend", font=("Arial", 16),
                 command=lambda: self.start_game("friend")).pack(pady=10)

    def start_game(self, mode):
        self.game_mode = mode
        self.mode_frame.destroy()
        self.setup_game()

    def setup_game(self):
        self.current_player = "X"
        self.winner = False
        self.buttons = []

        # Create game grid
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24),
                             width=5, height=2,
                             command=lambda x=i: self.button_click(x))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Status label
        self.label = tk.Label(self.root, text="Player X's turn", font=("Arial", 24))
        self.label.grid(row=3, column=0, columnspan=3)

        # Control buttons
        self.control_frame = tk.Frame(self.root)
        self.control_frame.grid(row=4, column=0, columnspan=3)
        
        tk.Button(self.control_frame, text="New Game", font=("Arial", 16),
                 command=self.reset_game).pack(side=tk.LEFT, padx=5)
        
        tk.Button(self.control_frame, text="Change Mode", font=("Arial", 16),
                 command=self.change_mode).pack(side=tk.LEFT, padx=5)
        
        tk.Button(self.control_frame, text="Quit", font=("Arial", 16),
                 command=self.root.quit).pack(side=tk.LEFT, padx=5)

    def button_click(self, index):
        if self.buttons[index]["text"] == "" and not self.winner:
            self.buttons[index]["text"] = self.current_player
            
            if self.check_winner():
                winner = "You" if self.current_player == "X" and self.game_mode == "computer" else \
                        "Computer" if self.current_player == "O" and self.game_mode == "computer" else \
                        f"Player {self.current_player}"
                self.game_over(f"{winner} wins!")
                return
                
            if self.check_tie():
                self.game_over("It's a tie!")
                return
                
            self.current_player = "O" if self.current_player == "X" else "X"
            self.update_label()
            
            if self.game_mode == "computer" and self.current_player == "O":
                self.root.after(500, self.computer_move)

    def computer_move(self):
        empty_spots = [i for i, button in enumerate(self.buttons) if button["text"] == ""]
        if empty_spots:
            self.button_click(random.choice(empty_spots))

    def check_winner(self):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for combo in wins:
            if self.buttons[combo[0]]["text"] == self.buttons[combo[1]]["text"] == \
               self.buttons[combo[2]]["text"] != "":
                for i in combo:
                    self.buttons[i].config(bg="green")
                self.winner = True
                return True
        return False

    def check_tie(self):
        return all(button["text"] != "" for button in self.buttons)

    def update_label(self):
        if self.game_mode == "computer":
            self.label.config(text="Computer's turn" if self.current_player == "O" else "Your turn")
        else:
            self.label.config(text=f"Player {self.current_player}'s turn")

    def game_over(self, message):
        answer = messagebox.askyesno("Game Over", f"{message}\nPlay again?")
        if answer:
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.current_player = "X"
        self.winner = False
        for button in self.buttons:
            button.config(text="", bg="systemButtonFace")
        self.update_label()

    def change_mode(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_mode_selection()

    def run(self):
        self.root.mainloop()

# Start the game
game = TicTacToe()
game.run()

