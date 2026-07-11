# Task2_codsoft
#TicTacToe AI versionized

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe AI")
root.geometry("400x450")
root.resizable(False, False)

# Heading
title = tk.Label(root, text="Tic-Tac-Toe AI", font=("Arial", 20, "bold"))
title.pack(pady=10)
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

current_player = "X"
game_over = False

def check_winner():
   # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
        # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    # Check second diagonal
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

def board_full():
    for row in board:
        if "" in row:
            return False
    return True

def button_click(row, col):
    global current_player,game_over
    if game_over:
        return
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col]["text"] = current_player

        print(board)

        winner = check_winner()

        if winner:
            print(f"{winner} Wins!")
            game_over = True
        elif board_full():
            print("Draw!")
            game_over = True   
        if not winner and not board_full() and not game_over:
            current_player = "O"
            ai_move()
# Frame for the board
board_frame = tk.Frame(root)
board_frame.pack()

buttons = []

# Create 3x3 buttons
for row in range(3):
    row_buttons = []
    for col in range(3):
        button = tk.Button(
            board_frame,
            text="",
            font=("Arial", 24, "bold"),
            width=5,
            height=2,
            command=lambda r=row, c=col: button_click(r, c)
        )
        button.grid(row=row, column=col)
        row_buttons.append(button)

    buttons.append(row_buttons)
def restart_game():
    global board, current_player, game_over

    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    current_player = "X"
    game_over = False

    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
def ai_move():
    global current_player, game_over

    if game_over:
        return

    move = best_move()

    if move:
     row, col = move

     board[row][col] = "O"
     buttons[row][col]["text"] = "O"

    winner = check_winner()
    if winner == "O":
     print("AI Wins!")
     game_over = True

    elif board_full():
     print("Draw!")
     game_over = True

    current_player = "X"

def minimax(board, is_maximizing):

    winner = check_winner()

    if winner == "O":
        return 1

    elif winner == "X":
        return -1

    elif board_full():
        return 0

    if is_maximizing:

        best_score = -1000

        for row in range(3):
            for col in range(3):

                if board[row][col] == "":

                    board[row][col] = "O"

                    score = minimax(board, False)

                    board[row][col] = ""

                    best_score = max(score, best_score)

        return best_score

    else:

        best_score = 1000

        for row in range(3):
            for col in range(3):

                if board[row][col] == "":

                    board[row][col] = "X"

                    score = minimax(board, True)

                    board[row][col] = ""

                    best_score = min(score, best_score)

        return best_score

def best_move():

    best_score = -1000
    move = None

    for row in range(3):
        for col in range(3):

            if board[row][col] == "":

                board[row][col] = "O"

                score = minimax(board, False)

                board[row][col] = ""

                if score > best_score:
                    best_score = score
                    move = (row, col)

    return move                       
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14),
    command=restart_game
)

restart_button.pack(pady=10)
# initialize the board
restart_game()           
# Start the GUI
root.mainloop()