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
        x = random.randint(10, 215)
        y = random.randint(10, 215)
        #size = random.randint(10, 200)
        dur = random.randint(0, 50)
        return x, y, x + dur, x + dur

    def paint(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
