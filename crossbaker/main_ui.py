#/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import crossbaker

try:
    from PySide2 import QtCore, QtGui, QtWidgets
except:
    try:
        from PySide2 import QtCore, QtGui
        QtWidgets = QtGui
    except:
        sys.exit()

class UI(object):
    def __init__(self):
        pass

    def setupUI(self):
        pass

    def reTranslateUI(self):
        pass