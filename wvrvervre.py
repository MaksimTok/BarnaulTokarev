import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = 10
        self.y = 10

    def initUI(self):
        self.resize(500, 500)
        self.show()

    def paintEvent(self, e):
        self.paint = QPainter()
        self.paint.begin(self)
        self.x += 10
        self.y += 10
        self.paint.drawEllipse(self.x, self.y, 10, 10)
        self.paint.end()

    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
