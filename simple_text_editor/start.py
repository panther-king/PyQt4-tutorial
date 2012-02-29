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

    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            text = open(self.filename).read()
            self.ui.editor_window.setText(text)

    def file_save(self):
        from os.path import isfile
        if isfile(self.filename):
            import codecs
            s = codecs.open(self.filename, "w", "utf-8")
            s.write(unicode(self.ui.editor_window.toPlainText()))
            s.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())

