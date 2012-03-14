#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from timer import Ui_TimerWindow


class timers(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(timers, self).__init__(parent)
        self.ui = Ui_TimerWindow()
        self.ui.setupUi(self)
        self.ctimer = QtCore.QTimer()
        self.stimer = QtCore.QTimer()

        # buttons
        QtCore.QObject.connect(self.ui.constant, QtCore.SIGNAL("clicked()"), self.constant)
        QtCore.QObject.connect(self.ui.single, QtCore.SIGNAL("clicked()"), self.single)

        # constant timer
        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"), self.constantUpdate)

        QtCore.QMetaObject.connectSlotsByName(self)

    def constant(self):
        """
        Start the constant timer
        """
        self.ctimer.start(1)

    def constantUpdate(self):
        """
        slot for constant timer timeout
        """
        val = self.ui.constantProgress.value() + 1
        if val > 100:
            val = 0
        self.ui.constantProgress.setValue(val)

    def single(self):
        """
        run singleShot timer after button push
        """
        self.stimer.singleShot(1000, self.singleUpdate)

    def singleUpdate(self):
        """
        Slot for singleShot timer timeout
        """
        val = self.ui.singleProgress.value() + 10
        if val > 100:
            val = 0
        self.ui.singleProgress.setValue(val)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = timers()
    myapp.show()
    sys.exit(app.exec_())

