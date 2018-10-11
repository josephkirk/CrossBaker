#/usr/bin/env python
# -*- coding: utf-8 -*-

_name = "MeshBaker"
_version = 1
_revision = 5
_author = "Nguyen Phi Hung"
_company = "Virtuos-Sparx"
import json
try:
    from PySide2 import QtCore, QtGui, QtWidgets
except ImportError:
    from PySide import QtCore, QtGui
    QtWidgets = QtGui
import logging
import utils as ul
import sys
import os
import inspect
from collections import OrderedDict
from enums import *
#

from utils import readLocalFile, getScriptDir
import subprocess

#
Config = readLocalFile("config.json")
ExportSetting = readLocalFile("exportSetting.json")
BakerPath = Config.get(ExportSetting["baker"])
#
print(getScriptDir())