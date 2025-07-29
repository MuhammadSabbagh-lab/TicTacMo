#Import Tinker
import tkinter as tk
from tkinter import messagebox

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Building the table in CLI

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Checking Wins/Draw
def check_win(board):
# - Checking Row Win
    for row in board: 
        if row[0] == row[1] == row[2] != " ":
            return True
# - Checking Column Win
    for c in range(3):
        if board [0][c] == board [1][c] == board [2][c] != " ":
            return True
# - Checking Diagonal Win
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True    
    return False
def check_draw(board):
    for row in board:
        if " " in row:
            return False
# - no blanks + no win -> draw
    return not check_win(board)

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Displaying Table in GUI

# define self.root
# root is the tinker window object
# self.root.title sets the title of the window
# self.current: keeps track of turns
# self.board: stores the game state using "create_board()"
# self.buttons: stores references to each button (3x3)
#calls self.build.gui() to draw the grid

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Mo")
        self.current = "X"
        self.board = create_board()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.build_gui()

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Defining the make_move function

# loops through "r" (rows) and "c" (column) indices
# creates a button, large text, fixed size, calls self.make_move(r, c) when clicked
# .grid() places button in 3x3 layout 
# stores each button in self.buttons to update later

    def build_gui(self):
        for r in range(3):
            for c in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial", 36), width=5, height=2,
                                command=lambda r=r, c=c: self.make_move(r, c))
                btn.grid(row=r, column=c)
                self.buttons[r][c] = btn

# make_move() - When a player clicks a cell
# If Cell is already filled, return, aka, do nothing           
    def make_move(self, r, c):
        if self.board[r][c] != " ":
            messagebox.showwarning("Invalid Move")
            return 

# If Cell is already filled, ignore the click
# Self.current is "X" or "O" depending on turn, for example, if X's turn, and they click row 1, column 2 = self.board[1][2] = "X"
# self.buttons is updating the button which is shown by config(text=...)
# “Put the current player’s letter in the board data AND in the button visual.”
        self.board[r][c] = self.current
        self.buttons[r][c].config(text=self.current)


# Check if player has won/draw 
# if game ends then show pop-up and reset board
# if not, switch turns

        if check_win(self.board):
            messagebox.showinfo("Game Over", f"Player {self.current} wins!")
            self.reset()
        elif check_draw(self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset()
        else:
# Switch turns: if it was x, not it's O (AI)
# if current is now O, trigger the AI move after half a second 
            self.current = "O" if self.current == "X" else "X"
        if self.current == "O":
            self.root.after(500, self.ai_move)        

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#Building the AI Algorithm

# ai_move() - basic AI that plays as "O"
# Loops through the board and finds the first empty cell
# makes a move in that cell by calling make_move()

    def ai_move(self):
        for r in range(3):
            for c in range (3):
                if self.board[r][c] == " ":
                    self.make_move(r, c)
                    return
#---------------------------------------------------------------------------------------------------------------------------------------------------------

# Add resent function
# sets current player back to X
# re-creates board 

    def reset(self):
        self.current = "X"
        self.board = create_board()
        for r in range(3):
            for c in range(3):
                self.buttons[r][c].config(text=" ")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

#  call the app

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
