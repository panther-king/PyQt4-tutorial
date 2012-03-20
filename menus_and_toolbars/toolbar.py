#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitAction = QtGui.QAction(QtGui.QIcon("exit.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Toolbar")
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
