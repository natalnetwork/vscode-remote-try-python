class GameController:
    def __init__(self, model, view, ai):
        self.model = model
        self.view = view
        self.ai = ai
        self.current_player = 'human'

    def start_game(self):
        self.model.reset_game()
        self.view.render_board(self.model.board)
        self.view.display_message("Das Spiel hat begonnen!")

    def make_move(self, x, y):
        if self.model.is_valid_move(x, y):
            self.model.update_board(x, y, self.current_player)
            if self.check_winner():
                self.view.display_message(f"{self.current_player} hat gewonnen!")
                return
            self.switch_player()
            self.ai_move()

    def ai_move(self):
        x, y = self.ai.calculate_move(self.model.board)
        self.make_move(x, y)

    def switch_player(self):
        self.current_player = 'ai' if self.current_player == 'human' else 'human'

    def check_winner(self):
        return self.model.check_winner(self.current_player)