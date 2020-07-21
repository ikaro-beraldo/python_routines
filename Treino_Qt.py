#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:03:49 2020

@author: ikaro
"""

import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("Hello World!")
label.show()
app.exec_()

##

from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

app = QApplication.instance()
if app == None:
    app = QApplication([])
        
view = QQuickView()
url = QUrl("view.qml")

view.setSource(url)
view.show()
app.exec_()