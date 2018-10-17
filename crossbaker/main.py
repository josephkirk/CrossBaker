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
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from crossbaker.libs.assetmodels import AssetModel
import crossbaker
import application_rc

class Baker(QC.QObject):
    def __init__(self):
        super().__init__()

    @Slot(result=str)
    def run(self):
        crossbaker.bakers.current().run()

class Main:
    def __init__(self):
        app = QG.QGuiApplication( sys.argv )
        app.setAttribute(Qt.AA_EnableHighDpiScaling)
        app.setAttribute(Qt.AA_UseOpenGLES)

        engine = QML.QQmlApplicationEngine()
        engine.objectCreated.connect(self.setWindow)
        qmlFile = os.path.join( os.path.dirname(__file__), "ui/main.qml" )
        headers = ("Title", "Description")

        file = QtCore.QFile(os.path.join( os.path.dirname(__file__), "samples/editabletreemodel/default.txt" ))
        file.open(QtCore.QIODevice.ReadOnly)
        assetModel = AssetModel(headers, str(file.readAll()))

        # file = os.path.join( os.path.dirname(__file__), "config/layers.json" )
        # with open(file, "r") as readfile:
        #     assetModel = json.load(readfile)
        bakers = Baker()
        root = engine.rootContext()
        root.setContextProperty("assetModel", assetModel)
        root.setContextProperty("bakers", bakers)
        engine.load(QC.QUrl.fromLocalFile( os.path.abspath( qmlFile ) ))
        # root().contextObject().show()
        # engine.show()
        self.show()
        app.exec_()

    def show(self):
        if self.window:
            self.window.flags = Qt.Window | Qt.WindowStaysOnTopHint
            getattr(self.window,"raise")()

    def setWindow(self, win, url):
        self.window = win

if __name__ == '__main__':
    main = Main()
