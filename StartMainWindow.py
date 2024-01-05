import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QColor, QPainter, QBrush, QPen
from PyQt6 import QtCore
from PyQt6.QtCore import Qt

class RoundedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False

        self.setWindowTitle("Закругленное окно")
        self.setGeometry(100,100,600,400)
        label = QLabel('Перетащите окно по экрану', self)
        label.move(50, 50)

        # Устанавливаем флаг Qt.WindowMove для возможности перетаскивания окна
        self.setFlag(True)

        self.show()

    def setFlag(self, value):
        self.flag = value

if __name__ == '__main__':
    app = QApplication(sys.argv)
    roundedWindow = RoundedWindow()
    roundedWindow.show()
    sys.exit(app.exec())