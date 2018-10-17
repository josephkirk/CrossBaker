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

class ConfigModel (QC.QAbstractListModel):
    MyRole = Qt.UserRole + 1

    def __init__(self, parent = None):
        super().__init__(parent)
        self._data = []
        self.populate()

    def roleNames(self):
        roles = {
            ConfigModel.MyRole : 'apppath',
            Qt.DisplayRole : 'appname'
        }
        return roles

    def rowCount(self, index):
        return len(self._data)

    def data(self, index, role):
        d = self._data[index.row()]

        if role == Qt.DisplayRole:
            return d['appname']
        elif role == Qt.DecorationRole:
            return Qt.black
        elif role == ConfigModel.MyRole:
            return d['apppath']
        return None

    def populate(self):
        for bname, bpath in crossbaker.bakers.allBakers().items():
            self._data.append({'appname':bname, 'apppath':bpath})

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
        configs = ConfigModel()
        root = engine.rootContext()

        root.setContextProperty("bakerconfigs", configs)
        root.setContextProperty("assetModel", assetModel)
        root.setContextProperty("baker", bakers)
        root.setContextProperty("bakers", crossbaker.bakers.bakernames())

        engine.load(QC.QUrl.fromLocalFile( os.path.abspath( qmlFile ) ))
        if not engine.rootObjects():
            sys.exit()
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
