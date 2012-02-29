# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Wed Feb 29 12:47:59 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(800, 600)
        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(10, 2, 391, 31))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(414, 2, 381, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.editor_window = QtGui.QTextEdit(self.centralwidget)
        self.editor_window.setGeometry(QtCore.QRect(10, 40, 781, 531))
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        notepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(notepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        notepad.setStatusBar(self.statusbar)

        self.retranslateUi(notepad)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(QtGui.QApplication.translate("notepad", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open.setText(QtGui.QApplication.translate("notepad", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("notepad", "Close", None, QtGui.QApplication.UnicodeUTF8))

