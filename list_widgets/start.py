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

        # All packages
        self.ui.allList.setColumnWidth(0, 200)
        self.ui.allList.setColumnWidth(1, 200)

        packages = yolklib.Distributions()
        for pkg in packages.get_distributions("all"):
            a = QtGui.QTreeWidgetItem(self.ui.allList)
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

        # Active packages
        self.ui.activeList.setColumnWidth(0, 200)
        self.ui.activeList.setColumnWidth(1, 200)

        for pkg in packages.get_distributions("active"):
            a = QtGui.QTreeWidgetItem(self.ui.activeList)
            pk = str(pkg[0]).split(" ")
            a.setText(0, pk[0])
            a.setText(1, pk[1])
            a.setText(2, "Active")

        # Not active packages
        self.ui.notActiveList.setColumnWidth(0, 200)
        self.ui.notActiveList.setColumnWidth(1, 200)

        for pkg in packages.get_distributions("nonactive"):
            a = QtGui.QTreeWidgetItem(self.ui.notActiveList)
            pk = str(pkg[0]).split(" ")
            a.setText(0, pk[0])
            a.setText(1, pk[1])
            a.setText(2, "Not Active")

        # Signals
        QtCore.QObject.connect(self.ui.pkgTabs, QtCore.SIGNAL("currentChanged(int)"), self.tab_change)

    def tab_change(self, tab_id):
        if tab_id == 0:
            self.ui.infoLabel.setText("<b>QYolk</b>: Browsing all installed cheeseshop packages")
        elif tab_id == 1:
            self.ui.infoLabel.setText("<b>QYolk</b>: Browsing active packages")
        elif tab_id == 2:
            self.ui.infoLabel.setText("<b>QYolk</b>: Browsing not active packages (older versions)")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())

