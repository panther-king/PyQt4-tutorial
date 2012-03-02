# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created: Fri Mar 02 12:45:24 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QYolk(object):
    def setupUi(self, QYolk):
        QYolk.setObjectName(_fromUtf8("QYolk"))
        QYolk.resize(800, 600)
        self.centralwidget = QtGui.QWidget(QYolk)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        QYolk.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QYolk)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QYolk.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QYolk)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QYolk.setStatusBar(self.statusbar)

        self.retranslateUi(QYolk)
        QtCore.QMetaObject.connectSlotsByName(QYolk)

    def retranslateUi(self, QYolk):
        QYolk.setWindowTitle(QtGui.QApplication.translate("QYolk", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("QYolk", "Col0", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(1, QtGui.QApplication.translate("QYolk", "Col1", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(2, QtGui.QApplication.translate("QYolk", "Col2", None, QtGui.QApplication.UnicodeUTF8))

