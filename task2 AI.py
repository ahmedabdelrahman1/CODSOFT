import random
import copy

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize the board
        
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def check_winner(self, board, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(board[i*3 + j] == player for j in range(3)):
                return 1 if player == 'O' else -1
            if all(board[j*3 + i] == player for j in range(3)):
                return 1 if player == 'O' else -1
        if all(board[i] == player for i in (0, 4, 8)) or all(board[i] == player for i in (2, 4, 6)):
            return 1 if player == 'O' else -1
        return 0

    def check_draw(self):
        return " " not in self.board

    def make_move(self, position, player):
        self.board[position] = player

    def copy(self):
        return copy.deepcopy(self)

    def get_best_move(self):
        best_score = -2
        move = -1
        for i in self.available_moves():
            temp_board = self.copy()
            temp_board.make_move(i, 'O')
            score = temp_board.minimax(0, False)
            if score > best_score:
                best_score = score
                move = i
        return move

    def minimax(self, depth, is_maximizing):
        if self.check_winner(self.board, 'O'):
            return 1
        elif self.check_winner(self.board, 'X'):
            return -1
        elif self.check_draw():
            return 0

        if is_maximizing:
            best_score = -2
            for i in self.available_moves():
                temp_board = self.copy()
                temp_board.make_move(i, 'O')
                score = temp_board.minimax(depth + 1, False)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = 2
            for i in self.available_moves():
                temp_board = self.copy()
                temp_board.make_move(i, 'X')
                score = temp_board.minimax(depth + 1, True)
                best_score = min(score, best_score)
            return best_score

    def heuristic_evaluation(self, board):
        score = 0

        # Check rows, columns, and diagonals
        for i in range(3):
            row = board[i*3:(i+1)*3]
            col = [board[j*3 + i] for j in range(3)]
            if all(spot == 'O' for spot in row):
                score += 1
            if all(spot == 'X' for spot in row):
                score -= 1
            if all(spot == 'O' for spot in col):
                score += 1
            if all(spot == 'X' for spot in col):
                score -= 1
        if all(board[i] == 'O' for i in (0, 4, 8)):
            score += 1
        if all(board[i] == 'X' for i in (0, 4, 8)):
            score -= 1
        if all(board[i] == 'O' for i in (2, 4, 6)):
            score += 1
        if all(board[i] == 'X' for i in (2, 4, 6)):
            score -= 1

        return score

    def evaluate_board(self):
        return self.heuristic_evaluation(self.board)

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()

        while True:
            # Human player's turn
            human_move = int(input("Enter your move (0-8): "))
            if human_move not in self.available_moves():
                print("Invalid move. Try again.")
                continue
            self.make_move(human_move, 'X')
            self.print_board()

            # Check if human player wins
            if self.check_winner(self.board, 'X'):
                print("Congratulations! You win!")
                break

            # Check if it's a draw
            if self.check_draw():
                print("It's a draw!")
                break

            # AI player's turn
            print("AI is making a move...")
            ai_move = self.get_best_move()
            self.make_move(ai_move, 'O')
            self.print_board()

            # Check if AI wins
            if self.check_winner(self.board, 'O'):
                print("AI wins! Better luck next time.")
                break

            # Check if it's a draw
            if self.check_draw():
                print("It's a draw!")
                break

xando = TicTacToe()

# Call the play_game method to start playing the game
xando.play_game()
