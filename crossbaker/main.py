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
from libs.assetmodels import AssetModel
import application_rc

def main():
    app = QG.QGuiApplication( sys.argv )
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    app.setAttribute(Qt.AA_UseOpenGLES)

    engine = QML.QQmlApplicationEngine()
    qmlFile = os.path.join( os.path.dirname(__file__), "ui/main.qml" )
    # context = QML.QQmlContext(engine.rootContext())
    headers = ("Title", "Description")

    file = QtCore.QFile(os.path.join( os.path.dirname(__file__), "samples/editabletreemodel/default.txt" ))
    file.open(QtCore.QIODevice.ReadOnly)
    # print(str(file.readAll()))
    assetModel = AssetModel(headers, str(file.readAll()))
    engine.load(QC.QUrl.fromLocalFile( os.path.abspath( qmlFile ) ))
    engine.rootContext().setContextProperty("assetModel", assetModel)
    # context.setContextProperty("assetModel", assetModel)
    # component.loadUrl(QC.QUrl.fromLocalFile( os.path.abspath( qmlFile ) ))
    # component = QML.QQmlComponent(engine.rootContext())
    # component.create(context)
    return app.exec_()

if __name__ == '__main__':
    main()