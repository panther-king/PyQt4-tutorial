#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui


class FileManagerWidget(QtGui.QListWidget):

    def __init__(self, parent=None):
        """
        QListWidget with handling of mouse events - left and right clicks
        """
        super(FileManagerWidget, self).__init__(parent)

        # Configure the items list
        self.setViewMode(QtGui.QListView.IconMode)
        self.setLayoutMode(QtGui.QListView.SinglePass)
        self.setResizeMode(QtGui.QListView.Adjust)
        self.setGridSize(QtCore.QSize(75, 75))

    def mouseReleaseEvent(self, event):
        """
        mouse button release event
        """
        button = event.button()

        # select an item on which we clicked
        item = self.itemAt(event.x(), event.y())
        if item:
            self.setCurrentItem(item)
            if button == 1:
                print "SIMPLE LEFT CLICK"

    def mousePressEvent(self, event):
        """
        mouse clicks events
        """
        button = event.button()

        item = self.itemAt(event.x(), event.y())
        if item:
            # select the item we clicked
            self.setCurrentItem(item)
            if button == 1:
                print "LEFT CLICK-DRAG"
            if button == 2:
                print "RIGHT CLICK"


app = QtGui.QApplication(sys.argv)


f = FileManagerWidget()
for i in range(1, 20):
    f.addItem(unicode(i))
f.show()

sys.exit(app.exec_())

