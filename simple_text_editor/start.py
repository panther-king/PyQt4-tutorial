#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui
from editor import Ui_notepad


class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_notepad()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.file_dialog)
        QtCore.QObject.connect(self.ui.button_save, QtCore.SIGNAL("clicked()"), self.file_save)
        QtCore.QObject.connect(self.ui.editor_window, QtCore.SIGNAL("textChanged()"), self.enable_save)

    def enable_save(self):
        self.ui.button_save.setEnabled(True)

    def file_dialog(self):
        response = False
        SAVE = u"保存"
        DISCARD = u"保存せずに終了"
        CANCEL = u"キャンセル"

        if self.ui.button_save.isEnabled() and self.filename:
            message = QtGui.QMessageBox(self)
            message.setText(u"内容が変更されています。保存しますか？")
            message.setWindowTitle("Notepad")
            message.setIcon(QtGui.QMessageBox.Question)
            message.addButton(SAVE, QtGui.QMessageBox.AcceptRole)
            message.addButton(DISCARD, QtGui.QMessageBox.DestructiveRole)
            message.addButton(CANCEL, QtGui.QMessageBox.RejectRole)
            message.setDetailedText(str(self.filename) + u"の変更が保存されていません。")
            message.exec_()
            response = message.clickedButton().text()

            if response == SAVE:
                self.file_save()
                self.ui.button_save.setEnabled(False)
            elif response == DISCARD:
                self.ui.button_save.setEnabled(False)

        if response != CANCEL:
            fd = QtGui.QFileDialog(self)
            self.filename = fd.getOpenFileName()
            from os.path import isfile
            if isfile(self.filename):
                import codecs
                s = codecs.open(self.filename, "r", "utf-8").read()
                self.ui.editor_window.setPlainText(s)
                self.ui.button_save.setEnabled(False)

    def file_save(self):
        from os.path import isfile
        if isfile(self.filename):
            import codecs
            s = codecs.open(self.filename, "w", "utf-8")
            s.write(unicode(self.ui.editor_window.toPlainText()))
            s.close()
            self.ui.button_save.setEnabled(False)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())

