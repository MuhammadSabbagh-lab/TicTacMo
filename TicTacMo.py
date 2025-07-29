        #Building the table
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]
def display_board(board):
    print()
    rows = [" | ".join(r) for r in board]
    width = len(rows[0])
    for i, row_str in enumerate(rows):
        print(row_str) 
        if i < len(rows) - 1:
            print("-" * width)

        # Checking Wins/Draw
def check_win(board):
#Checking Row Win
    for row in board: 
        if row[0] == row[1] == row[2] != " ":
            return True
#Checking Column Win
    for c in range(3):
        if board [0][c] == board [1][c] == board [2][c] != " ":
            return True
#Checking Diagonal Win
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True    
    return False
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    #no blanks + no win -> draw
    return not check_win(board)

        #Inputting "X" of "O"
def get_move(board):
    while True:
        choice = input("Choose a cell 1-9): ").strip()
        if not (choice.isdigit() and 1 <= int(choice) <=9):
            print("Invalid. Enter a number from 1 to 9")  
            continue
        pos = int(choice) - 1
        r, c = divmod(pos, 3)  
        if board[r][c] != " ":
            print ("Cell taken, choose another")  
            continue
        return r, c

        #Calling 
def main():
    board = create_board()
    current = "X"
    while True: 
        display_board(board)
        print(f"Player {current}'s turn")
        r, c = get_move(board)
        board[r][c] = current

        if check_win(board):
            display_board(board)
            print(f"Player {current} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("Draw!")
            break
        # Switch Players
        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    main()
