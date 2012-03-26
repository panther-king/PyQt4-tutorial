#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setFocusPolicy(QtCore.Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap("mute.png"))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QtGui.QSlider")
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap("mute.png"))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap("min.png"))
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap("med.png"))
        else:
            self.label.setPixmap(QtGui.QPixmap("max.png"))


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
