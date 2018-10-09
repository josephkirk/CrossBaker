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
import uiStyle as ui
import utils as ul
import sys
import os
import inspect
from collections import OrderedDict
from .enum import *
#
import pymel.core as pm

from utils import  readLocalFile
from subprocess import

#
Config = json.load(readLocalFile("config.json"))
MarmosetPath = Config["marmoset"]
PhotoshopPath = Config["photoshop"]
ExPython = Config["pythonex"]

#
