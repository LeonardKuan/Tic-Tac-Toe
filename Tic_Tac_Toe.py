import random

class TicTacToe:
    def __init__(self, difficulty, user_symbol):
        self.board = [[" " for _ in range(3)] for _ in range(3)] #  Structure [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.computer_symbol = "O"
        self.user_symbol = user_symbol
        self.difficulty = difficulty

    def print_board(self):
        for row in self.board:
            print(" | ".join(row)) # Joins each ' ' in board but separates them with '|' 
            print("-" * 9)

    def check_winner(self, player):
        # Checks all possibilities for a win
        for i in range(3):
            # The first condition checks for all horizontal wins, the second condition checks for all vertical wins
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        # The first condition checks for left-to-right diag win, the second condition checks for right-to-left diag win
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        # Simply checks if all cells in board is " "
        return all(all(cell != " " for cell in row) for row in self.board)

    def get_user_move(self):
        while True:
            try:
                move = int(input("Enter your move (1-9): "))
                # 1 <= move <= 9 is just a sanity check
                # board[(move - 1 // 3)] accesses the row of the TTT board, using //
                # [(move - 1) % 3] accesses the the column of the TTT board at the specified row, using %
                if 1 <= move <= 9 and self.board[(move - 1) // 3][(move - 1) % 3] == " ":
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def random_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        # available_moves will take the form of (i, j) to indicategetposition on board
        return random.choice(available_moves)

    def computer_optimal_move_dummies(self):
        return self.random_move()

    def computer_optimal_move_easy(self):
        move_types = [self.win_move, self.block_move, self.random_move]
        for move in move_types:
            if move() is not None:
                return move()

    def computer_optimal_move_med(self):
        move_types = [
            self.win_move, self.block_move, self.center_move,
            self.opposite_corner_move, self.random_move
        ]
        for move in move_types:
            if move() is not None:
                return move()

    def computer_optimal_move_hard(self):
        move_types = [
        self.win_move, self.block_move, self.fork_block_move,
        self.center_move, self.opposite_corner_move, self.random_move
        ]
        for move in move_types:
            if move() is not None:
                return move()

    def computer_optimal_move_god(self):
        move_types = [
            self.win_move, self.block_move, self.fork_block_move,
            self.center_move, self.opposite_corner_move,
            self.empty_corner_move, self.empty_side_move, self.random_move
        ]
        for move in move_types:
            if move() is not None:
                return move()

    def play(self):
        while True:
            self.print_board()

            # User move
            user_move = self.get_user_move()
            self.board[(user_move - 1) // 3][(user_move - 1) % 3] = self.user_symbol

            if self.check_winner(self.user_symbol):
                self.print_board()
                print("Congratulations! You win!")
                break
            elif self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            # Computer move
            print("Computer's move:")

            if self.difficulty == "Dummies":
                computer_move = self.computer_optimal_move_dummies()
            elif self.difficulty == "Easy":
                computer_move = self.computer_optimal_move_easy()
            elif self.difficulty == "Medium":
                computer_move = self.computer_optimal_move_med()
            elif self.difficulty == "Hard":
                computer_move = self.computer_optimal_move_hard()
            else:
                computer_move = self.computer_optimal_move_god()

            self.board[computer_move[0]][computer_move[1]] = self.computer_symbol

            if self.check_winner(self.computer_symbol):
                self.print_board()
                print("Computer wins! Better luck next time.")
                break
            elif self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

    def win_move(self):
        # Check for potential winning moves for the computer
        # Horizontal 1st matching
        for i in range(3):
            if all(self.board[i][j] == self.computer_symbol for j in range(2)) and self.board[i][2] == " ":
                return (i, 2)
        # Horizontal 2nd matching
        for i in range(3):
            if all(self.board[i][2 - j] == self.computer_symbol for j in range(2)) and self.board[i][0] == " ":
                return (i, 0)
        # Horizontal 3rd matching
        for i in range(3):
            if self.board[i][0] == self.computer_symbol and self.board[i][2] == self.computer_symbol and self.board[i][1] == " ":
                return (i, 1)
        # Vertical 1st matching
        for i in range(3):
            if all(self.board[j][i] == self.computer_symbol for j in range(2)) and self.board[2][i] == " ":
                return (2, i)
        # Vertical 2nd matching
        for i in range(3):
            if all(self.board[2 - j][i] == self.computer_symbol for j in range(2)) and self.board[0][i] == " ":
                return (0, i)
        # Vertical 3rd matching
        for i in range(3):
            if self.board[0][i] == self.computer_symbol and self.board[2][i] == self.computer_symbol and self.board[1][i] == " ":
                return (1, i)
        # Diagonal hard-code
        if all(self.board[i][i] == self.computer_symbol for i in range(2)) and self.board[2][2] == " ":
            return (2, 2)
        if all(self.board[i][i] == self.computer_symbol for i in range(1, 3)) and self.board[0][0] == " ":
            return (0, 0)
        if self.board[0][2] == self.computer_symbol and self.board[1][1] == self.computer_symbol and self.board[2][0] == " ":
            return (2, 0)
        if self.board[1][1] == self.computer_symbol and self.board[2][0] == self.computer_symbol and self.board[0][2] == " ":
            return (0, 2)
        return None

    def block_move(self):
        # Check for potential blocking moves against the user
        # Horizontal 1st matching
        for i in range(3):
            if all(self.board[i][j] == self.user_symbol for j in range(2)) and self.board[i][2] == " ":
                return (i, 2)
        # Horizontal 2nd matching
        for i in range(3):
            if all(self.board[i][2 - j] == self.user_symbol for j in range(2)) and self.board[i][0] == " ":
                return (i, 0)
        # Horizontal 3rd matching
        for i in range(3):
            if self.board[i][0] == self.user_symbol and self.board[i][2] == self.user_symbol and self.board[i][1] == " ":
                return (i, 1)
        # Vertical 1st matching
        for i in range(3):
            if all(self.board[j][i] == self.user_symbol for j in range(2)) and self.board[2][i] == " ":
                return (2, i)
        # Vertical 2nd matching
        for i in range(3):
            if all(self.board[2 - j][i] == self.user_symbol for j in range(2)) and self.board[0][i] == " ":
                return (0, i)
        # Vertical 3rd matching
        for i in range(3):
            if self.board[0][i] == self.user_symbol and self.board[2][i] == self.user_symbol and self.board[1][i] == " ":
                return (1, i)
        # Diagonal hard-code
        if all(self.board[i][i] == self.user_symbol for i in range(2)) and self.board[2][2] == " ":
            return (2, 2)
        if all(self.board[i][i] == self.user_symbol for i in range(1, 3)) and self.board[0][0] == " ":
            return (0, 0)
        if self.board[0][2] == self.user_symbol and self.board[1][1] == self.user_symbol and self.board[2][0] == " ":
            return (2, 0)
        if self.board[1][1] == self.user_symbol and self.board[2][0] == self.user_symbol and self.board[0][2] == " ":
            return (0, 2)
        return None

    def fork_block_move(self):
        # Blocking an opponent's fork: https://p-mckenzie.github.io/2020/07/30/tic-tac-toe/#fork-or-block-fork
        # Diagonal block
        if self.board[1][1] == self.computer_symbol and (
            (self.board[0][0] == self.user_symbol and self.board[2][2] == self.user_symbol and all(
                all(cell == " " for j, cell in enumerate(row) if (i, j) != (1, 1) and (i, j) != (0, 0) and (i, j) != (2, 2))
                for i, row in enumerate(self.board)
            ))
            or (self.board[0][2] == self.user_symbol and self.board[2][0] == self.user_symbol and all(
                all(cell == " " for j, cell in enumerate(row) if (i, j) != (1, 1) and (i, j) != (0, 2) and (i, j) != (2, 0))
                for i, row in enumerate(self.board)
            ))
        ):
            block_diagonal_fork = [(0, 1), (1, 0), (1, 2), (2, 1)]
            return random.choice(block_diagonal_fork)
        
        # Regular block
        if self.board[1][1] == self.computer_symbol:
            if (self.board[0][0] == self.user_symbol and self.board[2][1] == self.user_symbol) or (
                self.board[1][0] == self.user_symbol and self.board[2][2] == self.user_symbol
            ) or (self.board[1][0] == self.user_symbol and self.board[2][1] == self.user_symbol):
                return (2, 0)
            elif (self.board[0][1] == self.user_symbol and self.board[2][0] == self.user_symbol) or (
                self.board[0][1] == self.user_symbol and self.board[1][0] == self.user_symbol
            ) or (self.board[0][2] == self.user_symbol and self.board[1][0] == self.user_symbol):
                return (0, 0)
            elif (self.board[0][1] == self.user_symbol and self.board[1][2] == self.user_symbol) or (
                self.board[0][1] == self.user_symbol and self.board[2][2] == self.user_symbol
            ) or (self.board[0][0] == self.user_symbol and self.board[1][2] == self.user_symbol):
                return (0, 2)
            elif (self.board[1][2] == self.user_symbol and self.board[2][1] == self.user_symbol) or (
                self.board[0][2] == self.user_symbol and self.board[2][1] == self.user_symbol
            ) or (self.board[1][2] == self.user_symbol and self.board[2][0] == self.user_symbol):
                return (2, 2)
        return None

    def center_move(self):
        # Center move: Marks the center
        if self.board[1][1] == " ":
            return (1, 1)
        return None

    def opposite_corner_move(self):
        # Opposite corner: If the opponent is in the corner, the computer plays the opposite corner
        opposite_list1 = [[0, 0], [2, 2]]
        opposite_list2 = [[2, 0], [0, 2]]
        for i in range(len(opposite_list1)):
            if self.board[opposite_list1[i][0]][opposite_list1[i][1]] == self.user_symbol and self.board[opposite_list1[i - 1][0]][opposite_list1[i - 1][1]] == " ":
                return (opposite_list1[i - 1][0], opposite_list1[i - 1][1])
        for i in range(len(opposite_list2)):
            if self.board[opposite_list2[i][0]][opposite_list2[i][1]] == self.user_symbol and self.board[opposite_list2[i - 1][0]][opposite_list2[i - 1][1]] == " ":
                return (opposite_list2[i - 1][0], opposite_list2[i - 1][1])
        return None

    def empty_corner_move(self):
        # Empty corner: The computer plays in a corner square
        corner_list = [0, 2]
        for i in corner_list:
            for k in corner_list:
                if self.board[i][k] == " ":
                    return (i, k)
        return None

    def empty_side_move(self):
        # Empty side: The computer plays in a middle square on any of the four sides
        empty_list = [[1, 0], [0, 1], [1, 2], [2, 1]]
        for i in range(len(empty_list)):
            if self.board[empty_list[i][0]][empty_list[i][1]] == " ":
                return (empty_list[i][0], empty_list[i][1])
        return None

def play_game():
    print("Welcome to Tic-Tac-Toe!")

    difficulty_list = ["Dummies", "Easy", "Medium", "Hard", "Impossible"]
    alphanumeric_characters = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

    print("Which computer difficulty would you like to play against?")
    difficulty = input("Enter your chosen difficulty (Dummies / Easy / Medium / Hard / Impossible): ")
    while difficulty not in difficulty_list:
        print("That is not a valid difficulty setting.")
        difficulty = input("Enter your chosen difficulty (Dummies / Easy / Medium / Hard / Impossible): ")

    print("Which tic-tac-toe symbol would you like to use?")
    user_symbol = input("Enter your chosen symbol (alphanumeric characters only): ")
    while user_symbol not in alphanumeric_characters:
        print("That is not a valid symbol.")
        user_symbol = input("Enter your chosen symbol (alphanumeric characters only): ")

    game = TicTacToe(difficulty, user_symbol)
    game.play()

play_game()