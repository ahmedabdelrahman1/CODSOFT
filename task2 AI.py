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
    
    def evaluate_board(self, board):
        score = 0
        for i in range(3):
            if all(board[j] == 'O' for j in range(i*3, i*3+3)):
                score += 100
            if all(board[j] == 'X' for j in range(i*3, i*3+3)):
                score -= 100
        for i in range(3):
            if all(board[i+j*3] == 'O' for j in range(3)):
                score += 100
            if all(board[i+j*3] == 'X' for j in range(3)):
                score -= 100
        if all(board[i] == 'O' for i in (0, 4, 8)) or all(board[i] == 'O' for i in (2, 4, 6)):
            score += 1000
        if all(board[i] == 'X' for i in (0, 4, 8)) or all(board[i] == 'X' for i in (2, 4, 6)):
            score -= 1000
        return score
    
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
    
    def minimax(self, board, depth, alpha, beta, maximizing_player, max_depth):
        if depth == max_depth:
            return self.evaluate_board(board)
       
        if maximizing_player:
            max_eval = float('-inf')
            for move in self.available_moves():
                new_board = copy.deepcopy(board)
                new_board[move] = 'O'
                eval = self.minimax(new_board, depth + 1, alpha, beta,False,max_depth)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                new_board = copy.deepcopy(board)
                new_board[move] = 'X'
                eval = self.minimax(new_board, depth + 1, alpha, beta,True,max_depth)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
    
    def get_best_move(self):
        best_eval = float('inf')
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        for move in sorted(self.available_moves(), key=lambda x: self.minimax(copy.deepcopy(self.board), 0, alpha, beta, False, 5), reverse=True):
            new_board = copy.deepcopy(self.board)
            new_board[move] = 'O'
            evaluation = self.minimax(new_board, 0, alpha, beta, False, 5)
            if evaluation < best_eval:
                best_eval = evaluation
                best_move = move
        return best_move

def play_game():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")
    game.print_board()
    
    while True:
        # Human player's turn
        human_move = int(input("Enter your move (0-8): "))
        if human_move not in game.available_moves():
            print("Invalid move. Try again.")
            continue
        game.make_move(human_move, 'X')
        game.print_board()
        
        # Check if human player wins
        if game.check_winner(game.board, 'X'):
            print("Congratulations! You win!")
            break
        
        # Check if it's a draw
        if game.check_draw():
            print("It's a draw!")
            break
        
        # AI player's turn
        print("AI is making a move...")
        ai_move = game.get_best_move()
        game.make_move(ai_move, 'O')
        game.print_board()
        
        # Check if AI wins
        if game.check_winner(game.board, 'O'):
            print("AI wins! Better luck next time.")
            break
        
        # Check if it's a draw
        if game.check_draw():
            print("It's a draw!")
            break

play_game()
