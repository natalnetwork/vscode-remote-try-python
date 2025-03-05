from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class GameView(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Schiffe Versenken")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.board_label = QLabel("Spielbrett")
        self.layout.addWidget(self.board_label)

        self.message_label = QLabel("")
        self.layout.addWidget(self.message_label)

        self.restart_button = QPushButton("Neues Spiel")
        self.restart_button.clicked.connect(self.restart_game)
        self.layout.addWidget(self.restart_button)

    def render_board(self, board):
        # Hier könnte der Code zum Rendern des Spielbretts stehen
        self.board_label.setText(str(board))

    def display_message(self, message):
        self.message_label.setText(message)

    def restart_game(self):
        # Hier könnte der Code zum Neustarten des Spiels stehen
        QMessageBox.information(self, "Neues Spiel", "Das Spiel wird neu gestartet.")