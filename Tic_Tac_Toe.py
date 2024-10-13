board = [" " for i in range(9)]
current_player = "X"

def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    print(row1)
    print(row2)
    print(row3)

def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def reset_game():
    global board, current_player
    board = [" " for i in range(9)]
    current_player = "X"

while True:
    print_board()
    choice = int(input(f"Player {current_player}, enter your move (1-9): ").strip())
    if board[choice - 1] == " ":
        board[choice - 1] = current_player
    else:
        print("Invalid move. Try again.")
        continue

    if check_winner(board, current_player):
        print_board()
        print(f"Player {current_player} wins!")
        new_game = input("Do you want a new game? (yes/no): ").strip().lower()
        if new_game == "yes":
            reset_game()
        else:
            break

    if " " not in board:
        print_board()
        print("It's a tie!")
        new_game = input("Do you want a new game? (yes/no): ").strip().lower()
        if new_game == "yes":
            reset_game()
        else:
            break

    # Switch player
    current_player = "O" if current_player == "X" else "X"