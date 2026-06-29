import math

class MinimaxAI:
    def __init__(self, ai_player, human_player):
        self.ai_player = ai_player
        self.human_player = human_player

    def get_best_move(self, board):
        """
        Determines the best possible move for the AI using the Minimax algorithm.
        """
        best_score = -math.inf
        best_move = None

        for i in range(9):
            if board[i] == "":
                board[i] = self.ai_player
                score = self.minimax(board, 0, False)
                board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def minimax(self, board, depth, is_maximizing):
        """
        The Minimax algorithm function. Recursively evaluates all possible board
        states to find the optimal move.
        """
        winner = self.check_winner(board)
        if winner == self.ai_player:
            # Prefer faster wins
            return 10 - depth
        elif winner == self.human_player:
            # Prefer slower losses if unavoidable
            return depth - 10
        elif "" not in board:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if board[i] == "":
                    board[i] = self.ai_player
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if board[i] == "":
                    board[i] = self.human_player
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, board):
        """
        Checks the board for a winner. Returns the winning player's symbol or None.
        """
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
            (0, 4, 8), (2, 4, 6)             # diagonals
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
                return board[combo[0]]
        return None
