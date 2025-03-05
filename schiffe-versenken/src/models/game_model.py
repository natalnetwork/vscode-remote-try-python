class GameModel:
    def __init__(self):
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = []

    def place_ship(self, ship, coordinates):
        # Logik zum Platzieren eines Schiffs auf dem Board
        pass

    def update_board(self, x, y, hit):
        # Logik zum Aktualisieren des Boards nach einem Zug
        pass

    def reset_game(self):
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = []