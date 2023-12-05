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
            return (i, 2)

    # Horizontal 2nd matching
    for i in range(3):
        if all(board[i][2 - j] == "O" for j in range(2)) and board[i][0] == " ":
            return (i, 0)
        
    # Horizontal 3rd matching     
    for i in range(3):
        if board[i][0] == "O" and board[i][2] == "O" and board[i][1] == " ":
            return (i, 1)
       
    # Vertical 1st matching
    for i in range(3):
        if all(board[j][i] == "O" for j in range(2)) and board[2][i] == " ":
            return (2, i)

    # Vertical 2nd matching
    for i in range(3):
        if all(board[2 - j][i] == "O" for j in range(2)) and board[0][i] == " ":
            return (0, i)
        
    # Vertical 3rd matching    
    for i in range(3):
        if board[0][i] == "O" and board[2][i] == "O" and board[1][i] == " ":
            return (1, i)
 
    # Diagonal hard-code
    if all(board[i][i] == "O" for i in range(2)) and board[2][2] == " ":
        return (2, 2)

    if all(board[i][i] == "O" for i in range(1, 3)) and board[0][0] == " ":
        return (0, 0)

    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == " ":
        return (2, 0)

    if board[1][1] == "O" and board[2][0] == "O" and board[0][2] == " ":
        return (0, 2)
    
    ### 2. Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
    
    # Horizontal 1st matching
    for i in range(3):
        if all(board[i][j] == "X" for j in range(2)) and board[i][2] == " ":
            return (i, 2)

    # Horizontal 2nd matching
    for i in range(3):
        if all(board[i][2 - j] == "X" for j in range(2)) and board[i][0] == " ":
            return (i, 0)
        
    # Horizontal 3rd matching     
    for i in range(3):
        if board[i][0] == "X" and board[i][2] == "X" and board[i][1] == " ":
            return (i, 1)

    # Vertical 1st matching
    for i in range(3):
        if all(board[j][i] == "X" for j in range(2)) and board[2][i] == " ":
            return (2, i)

    # Vertical 2nd matching
    for i in range(3):
        if all(board[2 - j][i] == "X" for j in range(2)) and board[0][i] == " ":
            return (0, i)
        
    # Vertical 3rd matching    
    for i in range(3):
        if board[0][i] == "X" and board[2][i] == "X" and board[1][i] == " ":
            return (1, i)

    # Diagonal hard-code
    if all(board[i][i] == "X" for i in range(2)) and board[2][2] == " ":
        return (2, 2)

    if all(board[i][i] == "X" for i in range(1, 3)) and board[0][0] == " ":
        return (0, 0)

    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == " ":
        return (2, 0)

    if board[1][1] == "X" and board[2][0] == "X" and board[0][2] == " ":
        return (0, 2)
    
    ### 4. Blocking an opponent's fork: https://p-mckenzie.github.io/2020/07/30/tic-tac-toe/#fork-or-block-fork

    # Diagonal block
    if board[1][1] == "O" and ((board[0][0] == "X" and board[2][2] == "X" and all(all(cell == " " for j, cell in enumerate(row) if (i, j) != (1, 1) and (i, j) != (0, 0) and (i, j) != (2, 2)) for i, row in enumerate(board))) or (board[0][2] == "X" and board[2][0] == "X" and all(all(cell == " " for j, cell in enumerate(row) if (i, j) != (1, 1) and (i, j) != (0, 2) and (i, j) != (2, 0)) for i, row in enumerate(board)))):
        block_diagonal_fork = [(0, 1), (1, 0), (1, 2), (2, 1)]
        return random.choice(block_diagonal_fork)

    # Regular block
    if board[1][1] == "O":
        if (board[0][0] == "X" and board[2][1] == "X") or (board[1][0] == "X" and board[2][2] == "X") or (board[1][0] == "X" and board[2][1] == "X"):
            return (2, 0)
        elif (board[0][1] == "X" and board[2][0] == "X") or (board[0][1] == "X" and board[1][0] == "X") or (board[0][2] == "X" and board[1][0] == "X"):
            return (0, 0)
        elif (board[0][1] == "X" and board[1][2] == "X") or (board[0][1] == "X" and board[2][2] == "X") or (board[0][0] == "X" and board[1][2] == "X"):
            return (0, 2)
        elif (board[1][2] == "X" and board[2][1] == "X") or (board[0][2] == "X" and board[2][1] == "X") or (board[1][2] == "X" and board[2][0] == "X"):
            return (2, 2)

    ### 5. Center: A player marks the center.
    if board[1][1] == " ":
        return (1, 1)
    
    ### 6. Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
    oppositeList1 = [[0, 0], [2, 2]]
    oppositeList2 = [[2, 0], [0, 2]]
    for i in range(len(oppositeList1)):
        if board[oppositeList1[i][0]][oppositeList1[i][1]] == "X" and board[oppositeList1[i-1][0]][oppositeList1[i-1][1]] == " ":
            return (oppositeList1[i-1][0], oppositeList1[i-1][1])
        
    for i in range(len(oppositeList2)):
        if board[oppositeList2[i][0]][oppositeList2[i][1]] == "X" and board[oppositeList2[i-1][0]][oppositeList2[i-1][1]] == " ":
            return (oppositeList2[i-1][0], oppositeList2[i-1][1])
    
    ### 7. Empty corner: The player plays in a corner square.
    cornerList = [0, 2]   
    for i in cornerList:
        for k in cornerList:
            if board[i][k] == " ":
                return (i, k)
    
    ### 8. Empty side: The player plays in a middle square on any of the four sides.
    emptyList = [[1, 0], [0, 1], [1, 2], [2, 1]]
    for i in range(len(emptyList)):
        if board[emptyList[i][0]][emptyList[i][1]] == " ":
            return (emptyList[i][0], emptyList[i][1])

    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    # available_moves will take the form of (i, j) to indicategetposition on board

    return random.choice(available_moves)

def clear_board(board):
    for i in range(0, 3):
        for k in range(0, 3):
            board[i][k] = " "

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)] #  Structure [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    random_computer_symbol = "X"
    computer_symbol = "O"

    # print("Welcome to Tic-Tac-Toe!")

    global count
    global computer_wins
    global random_computer_wins
    global ties

    count = 0
    computer_wins = 0
    random_computer_wins = 0
    ties = 0

    while count < 20000:
        # print_board(board)

        # Random_computer move
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
        random_computer_move = random.choice(available_moves)
        board[random_computer_move[0]][random_computer_move[1]] = random_computer_symbol

        if check_winner(board, random_computer_symbol):
            # print_board(board)
            # print("Congratulations! Random computer wins!")
            count += 1
            random_computer_wins += 1
            clear_board(board)
        elif is_board_full(board):
            # print_board(board)
            # print("It's a tie!")
            count += 1
            ties += 1
            clear_board(board)

        # Computer move
        # print("Computer's move:")
        computer_move = computer_optimal_move(board)
        board[computer_move[0]][computer_move[1]] = computer_symbol

        if check_winner(board, computer_symbol):
            # print_board(board)
            # print("Computer wins! Better luck next time.")
            count += 1
            computer_wins += 1
            clear_board(board)
        elif is_board_full(board):
            # print_board(board)
            # print("It's a tie!")
            count += 1
            ties += 1
            clear_board(board)

play_tic_tac_toe()

print("A total of " + str(count) + " games were played")
print("AI has won " + str(computer_wins) + " games")
print("Random computer has won " + str(random_computer_wins) + " games")
print("AI and random computer drew " + str(ties) + " games")