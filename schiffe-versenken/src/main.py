from PyQt5.QtWidgets import QApplication
import sys
from controllers.game_controller import GameController

def main():
    app = QApplication(sys.argv)
    controller = GameController()
    controller.start_game()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()