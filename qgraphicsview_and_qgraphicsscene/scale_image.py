#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ImageView(QGraphicsView):

    def __init__(self, parent=None, origPixmap=None):
        super(ImageView, self).__init__(parent)
        self.origPixmap = origPixmap
        QMetaObject.connectSlotsByName(self)

    def resizeEvent(self, event):
        """
        Handle the resize event
        """
        size = event.size()
        item = self.items()[0]

        # Using current pixmap after n-resizes would get really blurry image
        pixmap = self.origPixmap
        pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.centerOn(1.0, 1.0)
        item.setPixmap(pixmap)


app = QApplication(sys.argv)

pic = QPixmap("sample.jpg")
grview = ImageView(origPixmap=pic)

scene = QGraphicsScene()
scene.addPixmap(pic)

grview.setScene(scene)
grview.show()

sys.exit(app.exec_())
