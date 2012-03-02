#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from list import Ui_QYolk
from yolk import yolklib


class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_QYolk()
        self.ui.setupUi(self)

        self.ui.treeWidget.setColumnWidth(0, 200)
        self.ui.treeWidget.setColumnWidth(1, 100)

        packages = yolklib.Distributions()
        for pkg in packages.get_distributions("all"):
            a = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            pk = str(pkg[0]).split(" ")
            if pkg[1]:
                status = "Active"
            else:
                status = "Not Active"
                a.setTextColor(0, QtGui.QColor(128, 128, 128))
                a.setTextColor(1, QtGui.QColor(128, 128, 128))
                a.setTextColor(2, QtGui.QColor(128, 128, 128))
            a.setText(0, pk[0])
            a.setText(1, pk[1])
            a.setText(2, status)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())

