# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timer.ui'
#
# Created: Thu Mar 15 08:41:28 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TimerWindow(object):
    def setupUi(self, TimerWindow):
        TimerWindow.setObjectName(_fromUtf8("TimerWindow"))
        TimerWindow.resize(800, 153)
        self.centralwidget = QtGui.QWidget(TimerWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.constant = QtGui.QPushButton(self.centralwidget)
        self.constant.setGeometry(QtCore.QRect(10, 20, 131, 23))
        self.constant.setObjectName(_fromUtf8("constant"))
        self.single = QtGui.QPushButton(self.centralwidget)
        self.single.setGeometry(QtCore.QRect(10, 70, 131, 23))
        self.single.setObjectName(_fromUtf8("single"))
        self.constantProgress = QtGui.QProgressBar(self.centralwidget)
        self.constantProgress.setGeometry(QtCore.QRect(170, 20, 621, 23))
        self.constantProgress.setProperty("value", 0)
        self.constantProgress.setTextVisible(False)
        self.constantProgress.setObjectName(_fromUtf8("constantProgress"))
        self.singleProgress = QtGui.QProgressBar(self.centralwidget)
        self.singleProgress.setGeometry(QtCore.QRect(170, 70, 621, 23))
        self.singleProgress.setProperty("value", 0)
        self.singleProgress.setTextVisible(False)
        self.singleProgress.setInvertedAppearance(False)
        self.singleProgress.setObjectName(_fromUtf8("singleProgress"))
        TimerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TimerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        TimerWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TimerWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TimerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TimerWindow)
        QtCore.QMetaObject.connectSlotsByName(TimerWindow)

    def retranslateUi(self, TimerWindow):
        TimerWindow.setWindowTitle(QtGui.QApplication.translate("TimerWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.constant.setText(QtGui.QApplication.translate("TimerWindow", "ConstantTimer", None, QtGui.QApplication.UnicodeUTF8))
        self.single.setText(QtGui.QApplication.translate("TimerWindow", "SingleShotTimer", None, QtGui.QApplication.UnicodeUTF8))

