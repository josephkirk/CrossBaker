#/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    from PySide2.QtCore import Property, QObject, Signal, Slot
except:
    from PySide.QtCore import Property, QObject, Signal, Slot

from collections import namedtuple
from crossbaker import logger
import subprocess
import os

Size = namedtuple("Size", ["w","h"])

class App(QObject):
    def __init__(self, name, path, execmod=[]):
        super(App, self).__init__()
        #
        self._name = ""
        self._path = ""
        self._mod = []
        #
        self.name = name
        self.path = path
        self.mod = execmod

    def __str__(self):
        return self.path

    def __repr__(self):
        return "{}:{}:{}".format(self.name, self.path, self.mod)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = str(newName)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, newpath):
        self._path = str(newpath)

    @property
    def mod(self):
        return self._mod

    @mod.setter
    def mod(self, newmod):
        if hasattr(newmod, "__iter__"):
            self._mod = [str(mod) for mod in newmod]

    def getname(self):
        return self.name.capitalize()

    def setname(self, newName):
        self.name = newName

    def getpath(self):
        return self.path

    def setpath(self, newpath):
        self.path = newpath

    @Signal
    def nameChanged(self):
        pass

    @Signal
    def pathChanged(self):
        pass

    def run(self):
        logger.debug("exec {} with args: {}".format(self.path, self.mod))
        if os.path.exists(self.path):
            com = subprocess.Popen(
                ["{}".format(self.path)]+self.mod,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            return com.communicate()

    appname = Property(str, getname, setname, notify=nameChanged)
    apppath = Property(str, getpath, setpath, notify=pathChanged)

class BakerApp(App):
    def __init__(self, name, path, execmod=None):
        super(BakerApp, self).__init__(name, path)
        self.mod = execmod

    @property
    def mod(self):
        return self._mod

    @mod.setter
    def mod(self, newmod):
        if hasattr(newmod, "get"):
            self._mod = newmod

    def run(self):
        if hasattr(self.mod, "get"):
            logger.debug("exec {} with args: {}".format(self.name, self.mod.get()))
            com = subprocess.Popen(
                ["{}".format(self.path)]+self.mod.get(),
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            com.communicate()

class ImageApp(App):
    def __init__(self, name, path, execmod=[]):
        super(ImageApp, self).__init__(name, path, execmod)

    def run(self):
        super(ImageApp, self).run()