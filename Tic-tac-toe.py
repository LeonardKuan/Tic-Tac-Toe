import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9 and board[(move - 1) // 3][(move - 1) % 3] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(available_moves)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    user_symbol = "X"
    computer_symbol = "O"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        # User move
        user_move = get_user_move(board)
        board[(user_move - 1) // 3][(user_move - 1) % 3] = user_symbol

        # Check for a win or a tie
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
        computer_move = get_computer_move(board)
        board[computer_move[0]][computer_move[1]] = computer_symbol

        # Check for a win or a tie after computer's move
        if check_winner(board, computer_symbol):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()