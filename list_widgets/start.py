#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import pkg_resources
import cPickle

from os.path import isfile
from os.path import expanduser
from datetime import timedelta
from datetime import datetime

from PyQt4 import QtCore, QtGui
from yolk import yolklib
from yolk.cli import get_pkglist
from yolk.yolklib import get_highest_version, Distributions
from yolk.pypi import CheeseShop
from list import Ui_QYolk


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
        elif tab_id == 3:
            self.ui.infoLabel.setText("<b>QYolk</b>: Browsing available updates")


def get_fresh_updates(package_name="", version=""):
    userpath = expanduser("~")
    now = datetime.now()

    # Do we have a cache ?
    if isfile(userpath + "/.qyolk"):
        f = open(userpath + "/.qyolk", "r")
        cache = cPickle.load(f)
        check_time = now - timedelta(hours=24)
        if cache[0] > check_time:
            # fresh cache, use it
            return cache[1]

    # No cache, get updates and create the cache
    ret = []
    pypi = CheeseShop()
    dists = Distributions()
    for pkg in get_pkglist():
        for (dist, active) in dists.get_distributions("all", pkg, dists.get_highest_installed(pkg)):
            (project_name, versions) = pypi.query_versions_pypi(dist.project_name)
            if versions:
                newest = get_highest_version(versions)
                if newest != dist.version:
                    if pkg_resources.parse_version(dist.version) < pkg_resources.parse_version(newest):
                        ret.append([project_name, dist.version, newest])

    f = open(userpath + "/.qyolk", "w")
    cPickle.dump([now, ret], f)

    return ret


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())

