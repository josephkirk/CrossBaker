#/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from crossbaker import logger
import subprocess
import os

Size = namedtuple("Size", ["w","h"])

class BakerApp(object):
    def __init__(self, name, path, execmod=""):
        self.name = name
        self.path = os.path.normpath(path)
        self.mod = execmod


    def __str__(self):
        return self.path

    def __repr__(self):
        return "{}:{}".format(self.name, self.path)

    def run(self):
        logger.debug("exec {} with args: {}".format(self.name, self.mod.get()))
        com = subprocess.call(["{}".format(self.path)]+self.mod.get())
        # com.communicate()
