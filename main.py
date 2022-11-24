import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gitlesson_2.ui', self)
        self.btn_draw.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(*self.random_coords())
        qp.end()

    def random_coords(self):
        x = random.randint(10, 200)
        size = random.randint(10, 200)
        dur = random.randint(-150, 150)
        return x + dur, x + dur, x + size + dur, x + size + dur

    def paint(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
