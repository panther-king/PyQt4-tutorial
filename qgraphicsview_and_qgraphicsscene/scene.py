#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


app = QApplication(sys.argv)

grview = QGraphicsView()
scene = QGraphicsScene()
scene.addPixmap(QPixmap("sample.jpg"))
grview.setScene(scene)

grview.show()

sys.exit(app.exec_())
