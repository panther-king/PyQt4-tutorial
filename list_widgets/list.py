# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created: Sat Mar 03 09:09:07 2012
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
        self.pkgTabs = QtGui.QTabWidget(self.centralwidget)
        self.pkgTabs.setGeometry(QtCore.QRect(10, 10, 781, 551))
        self.pkgTabs.setObjectName(_fromUtf8("pkgTabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.allList = QtGui.QTreeWidget(self.tab)
        self.allList.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.allList.setObjectName(_fromUtf8("allList"))
        self.pkgTabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.activeList = QtGui.QTreeWidget(self.tab_2)
        self.activeList.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.activeList.setObjectName(_fromUtf8("activeList"))
        self.pkgTabs.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.notActiveList = QtGui.QTreeWidget(self.tab_3)
        self.notActiveList.setGeometry(QtCore.QRect(10, 10, 751, 501))
        self.notActiveList.setObjectName(_fromUtf8("notActiveList"))
        self.pkgTabs.addTab(self.tab_3, _fromUtf8(""))
        QYolk.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QYolk)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QYolk.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QYolk)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QYolk.setStatusBar(self.statusbar)

        self.retranslateUi(QYolk)
        self.pkgTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(QYolk)

    def retranslateUi(self, QYolk):
        QYolk.setWindowTitle(QtGui.QApplication.translate("QYolk", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.allList.headerItem().setText(0, QtGui.QApplication.translate("QYolk", "Col0", None, QtGui.QApplication.UnicodeUTF8))
        self.allList.headerItem().setText(1, QtGui.QApplication.translate("QYolk", "Col1", None, QtGui.QApplication.UnicodeUTF8))
        self.allList.headerItem().setText(2, QtGui.QApplication.translate("QYolk", "Col2", None, QtGui.QApplication.UnicodeUTF8))
        self.pkgTabs.setTabText(self.pkgTabs.indexOf(self.tab), QtGui.QApplication.translate("QYolk", "All Packages", None, QtGui.QApplication.UnicodeUTF8))
        self.activeList.headerItem().setText(0, QtGui.QApplication.translate("QYolk", "Col0", None, QtGui.QApplication.UnicodeUTF8))
        self.activeList.headerItem().setText(1, QtGui.QApplication.translate("QYolk", "Col1", None, QtGui.QApplication.UnicodeUTF8))
        self.activeList.headerItem().setText(2, QtGui.QApplication.translate("QYolk", "Col2", None, QtGui.QApplication.UnicodeUTF8))
        self.pkgTabs.setTabText(self.pkgTabs.indexOf(self.tab_2), QtGui.QApplication.translate("QYolk", "Active", None, QtGui.QApplication.UnicodeUTF8))
        self.notActiveList.headerItem().setText(0, QtGui.QApplication.translate("QYolk", "Col0", None, QtGui.QApplication.UnicodeUTF8))
        self.notActiveList.headerItem().setText(1, QtGui.QApplication.translate("QYolk", "Col1", None, QtGui.QApplication.UnicodeUTF8))
        self.notActiveList.headerItem().setText(2, QtGui.QApplication.translate("QYolk", "Col2", None, QtGui.QApplication.UnicodeUTF8))
        self.pkgTabs.setTabText(self.pkgTabs.indexOf(self.tab_3), QtGui.QApplication.translate("QYolk", "Not Active", None, QtGui.QApplication.UnicodeUTF8))

