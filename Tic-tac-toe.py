import random

def print_board(board):
    for row in board:
        print(" | ".join(row)) # Joins each ' ' in board but separates them with '|' 
        print("-" * 9)

def check_winner(board, player):
    # Checks all possibilities for a win
    for i in range(3):
        # The first condition checks for all horizontal wins, the second condition checks for all vertical wins
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # The first condition checks for left-to-right diag win, the second condition checks for right-to-left diag win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Simply checks if all cells in board is " "
    return all(all(cell != " " for cell in row) for row in board)

def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9 and board[(move - 1) // 3][(move - 1) % 3] == " ":
                # 1 <= move <= 9 is just a sanity check
                # board[(move - 1 // 3)] accesses the row of the TTT board, using //
                # [(move - 1) % 3] accesses the the column of the TTT board at the specified row, using %
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_optimal_move(board):
    # Horizontal 1st matching
    for i in range(3):
        if all(board[i][j] == "O" for j in range(2)) and board[i][2] == " ":
            return (i, 2)

    # Horizontal 2nd matching
    for i in range(3):
        if all(board[i][2 - j] == "O" for j in range(2)) and board[i][0] == " ":
            return (i, 0)

    # Vertical 1st matching
    for i in range(3):
        if all(board[j][i] == "O" for j in range(2)) and board[2][i] == " ":
            return (2, i)

    # Vertical 2nd matching
    for i in range(3):
        if all(board[2 - j][i] == "O" for j in range(2)) and board[0][i] == " ":
            return (0, i)

    # Diagonal hard-code
    if all(board[i][i] == "O" for i in range(2)) and board[2][2] == " ":
        return (2, 2)

    if all(board[i][i] == "O" for i in range(1, 3)) and board[0][0] == " ":
        return (0, 0)

    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == " ":
        return (2, 0)

    if board[1][1] == "O" and board[2][0] == "O" and board[0][2] == " ":
        return (0, 2)
    
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    # available_moves will take the form of (i, j) to indicate position on board

    return random.choice(available_moves)

def get_computer_move(board):
    computer_optimal_move(board)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)] #  Structure [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    user_symbol = "X"
    computer_symbol = "O"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        # User move
        user_move = get_user_move(board)
        board[(user_move - 1) // 3][(user_move - 1) % 3] = user_symbol

        if check_winner(board, user_symbol):
            print_board(board)
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Computer move
        print("Computer's move:")
        computer_move = computer_optimal_move(board)
        board[computer_move[0]][computer_move[1]] = computer_symbol

        if check_winner(board, computer_symbol):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

play_tic_tac_toe()