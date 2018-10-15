#/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import os
try:
    from PySide2 import QtCore, QtGui, QtWidgets, QtQml, QtQuick
except:
    try:
        from PySide2 import QtCore, QtGui, QtQml
        QtWidgets = QtGui
    except:
        sys.exit()

QC = QtCore
QG = QtGui
QW = QtWidgets
QML = QtQml
QQ = QtQuick
Qt = QC.Qt
Signal = QC.Signal
Slot = QC.Slot

import qml_rc

def main():
    app = QG.QGuiApplication( sys.argv )
    qmlFile = os.path.join( os.path.dirname(__file__), "ui/main.qml" )
    engine = QML.QQmlApplicationEngine(QC.QUrl.fromLocalFile( os.path.abspath( qmlFile ) ))
    return app.exec_()


if __name__ == '__main__':
    main()