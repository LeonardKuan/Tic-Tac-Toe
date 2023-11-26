# Customability: can introduce difficulty option, .wait() something, choose your own symbol

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
    ### 1. Win: If the player has two in a row, they can place a third to get three in a row.
    
    # Horizontal 1st matching
    for i in range(3):
        if all(board[i][j] == "O" for j in range(2)) and board[i][2] == " ":
            print("executed hori match")
            return (i, 2)

    # Horizontal 2nd matching
    for i in range(3):
        if all(board[i][2 - j] == "O" for j in range(2)) and board[i][0] == " ":
            print("executed hori match")
            return (i, 0)
        
    # Horizontal 3rd matching     
    for i in range(3):
        if board[i][0] == "O" and board[i][2] == "O" and board[i][1] == " ":
            print("executed hori match")
            return (i, 1)
       
    # Vertical 1st matching
    for i in range(3):
        if all(board[j][i] == "O" for j in range(2)) and board[2][i] == " ":
            print("executed vert match")
            return (2, i)

    # Vertical 2nd matching
    for i in range(3):
        if all(board[2 - j][i] == "O" for j in range(2)) and board[0][i] == " ":
            print("executed vert match")
            return (0, i)
        
    # Vertical 3rd matching    
    for i in range(3):
        if board[0][i] == "O" and board[2][i] == "O" and board[1][i] == " ":
            print("executed vert match")
            return (1, i)
 
    # Diagonal hard-code
    if all(board[i][i] == "O" for i in range(2)) and board[2][2] == " ":
        print("executed diag match")
        return (2, 2)

    if all(board[i][i] == "O" for i in range(1, 3)) and board[0][0] == " ":
        print("executed diag match")
        return (0, 0)

    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == " ":
        print("executed diag match")
        return (2, 0)

    if board[1][1] == "O" and board[2][0] == "O" and board[0][2] == " ":
        print("executed diag match")
        return (0, 2)
    
    ### 2. Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
    
    # Horizontal 1st matching
    for i in range(3):
        if all(board[i][j] == "X" for j in range(2)) and board[i][2] == " ":
            print("executed hori block")
            return (i, 2)

    # Horizontal 2nd matching
    for i in range(3):
        if all(board[i][2 - j] == "X" for j in range(2)) and board[i][0] == " ":
            print("executed hori block")
            return (i, 0)
        
    # Horizontal 3rd matching     
    for i in range(3):
        if board[i][0] == "X" and board[i][2] == "X" and board[i][1] == " ":
            print("executed hori block")
            return (i, 1)

    # Vertical 1st matching
    for i in range(3):
        if all(board[j][i] == "X" for j in range(2)) and board[2][i] == " ":
            print("executed vert block")
            return (2, i)

    # Vertical 2nd matching
    for i in range(3):
        if all(board[2 - j][i] == "X" for j in range(2)) and board[0][i] == " ":
            print("executed vert block")
            return (0, i)
        
    # Vertical 3rd matching    
    for i in range(3):
        if board[0][i] == "X" and board[2][i] == "X" and board[1][i] == " ":
            print("executed vert block")
            return (1, i)

    # Diagonal hard-code
    if all(board[i][i] == "X" for i in range(2)) and board[2][2] == " ":
        print("executed diag block")
        return (2, 2)

    if all(board[i][i] == "X" for i in range(1, 3)) and board[0][0] == " ":
        print("executed diag block")
        return (0, 0)

    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == " ":
        print("executed diag block")
        return (2, 0)

    if board[1][1] == "X" and board[2][0] == "X" and board[0][2] == " ":
        print("executed diag block")
        return (0, 2)
    
    ### 4. Blocking an opponent's fork: If there is only one possible fork for the opponent, 
    ### the player should block it. Otherwise, the player should block all forks in any way that 
    ### simultaneously allows them to make two in a row. Otherwise, the player should make a two 
    ### in a row to force the opponent into defending, as long as it does not result in them producing a fork. 
    ### For example, if "X" has two opposite corners and "O" has the center, "O" must not play a corner move to win. 
    ### (Playing a corner move in this scenario produces a fork for "X" to win.)
    
    # 4 possible combinations for a fork
    # center is filled with user (1, 1) == "X"
    # L shaped fork can be rotated 4 different ways
    # (0, 0), (2, 0), (2, 2) == "X" and 
     
    ### 5. Center: A player marks the center.
    if board[1][1] == " ":
        print("executed center")
        return (1, 1)
    
    ### 6. Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
    oppositeList1 = [[0, 0], [2, 2]]
    oppositeList2 = [[2, 0], [0, 2]]
    for i in range(len(oppositeList1)):
        if board[oppositeList1[i][0]][oppositeList1[i][1]] == "X" and board[oppositeList1[i-1][0]][oppositeList1[i-1][1]] == " ":
            print("executed oppo corner")
            return (oppositeList1[i-1][0], oppositeList1[i-1][1])
        
    for i in range(len(oppositeList2)):
        if board[oppositeList2[i][0]][oppositeList2[i][1]] == "X" and board[oppositeList2[i-1][0]][oppositeList2[i-1][1]] == " ":
            print("executed oppo corner")
            return (oppositeList2[i-1][0], oppositeList2[i-1][1])
    
    ### 7. Empty corner: The player plays in a corner square.
    cornerList = [0, 2]   
    for i in cornerList:
        for k in cornerList:
            if board[i][k] == " ":
                print("executed empty corner")
                return (i, k)
    
    ### 8. Empty side: The player plays in a middle square on any of the four sides.
    emptyList = [[1, 0], [0, 1], [1, 2], [2, 1]]
    for i in range(len(emptyList)):
        if board[emptyList[i][0]][emptyList[i][1]] == " ":
            print("executed empty side")
            return (emptyList[i][0], emptyList[i][1])

    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    # available_moves will take the form of (i, j) to indicategetposition on board

    return random.choice(available_moves)

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