import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Ship(QtWidgets.QGraphicsPixmapItem):
    def __init__(self, x, y, width, height, image_path):
        super().__init__()
        self.setPixmap(QtGui.QPixmap(image_path).scaled(width, height))
        self.setPos(x, y)

class Board(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QtWidgets.QGraphicsScene()
        self.setScene(self.scene)
        self.board_size = 10
        self.ship = Ship(0, 0, 64, 32, "ship.png")
        self.scene.addItem(self.ship)  # Fixed: addItem should be called on the scene
        self.drag = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag = True
            self.ship.setPos(event.scenePos())

    def mouseMoveEvent(self, event):
        if self.drag:
            self.ship.setPos(event.scenePos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag = False

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.setCentralWidget(self.board)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()