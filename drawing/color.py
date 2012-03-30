#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle("Colors")
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor("#D4D4D4")
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(25, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

