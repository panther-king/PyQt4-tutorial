#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *


app = QApplication(sys.argv)
w = QTextBrowser()

# DB type, host, user, password...
db = QSqlDatabase.addDatabase("QSQLITE")
db.setHostName("test.db")
db.setDatabaseName("test.db")
db.setUserName("admin")
db.setPassword("")
ok = db.open()

# True if connected
if ok:
    w.insertHtml("Connected to SQLite<br />")
else:
    w.insertHtml("ERROR connecting to SQLite<br />")

# do a query "on" a DB connection
query = QSqlQuery(db)
if query.exec_("SELECT * FROM fruit ORDER BY id"):
    w.insertHtml("<br />")
    while query.next():
        table = query.value(1).toString()
        w.insertHtml("%s<br />" % table)

    w.insertHtml("<br />")
    w.insertHtml("TOTAL %s ROWS" % query.size())


w.show()
sys.exit(app.exec_())

