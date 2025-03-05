class AI:
    def __init__(self):
        self.last_move = None

    def calculate_move(self, board):
        # Implement a simple AI strategy to make a move
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:  # Assuming 0 means empty
                    self.last_move = (x, y)
                    return self.last_move
        return None  # No valid moves available