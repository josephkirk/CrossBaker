#/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from crossbaker import logger
Size = namedtuple("Size", ["x","y"])

class BakerApp(object):
    def __init__(self, name, path, execmod=""):
        self.name = name
        self.path = path
        self.mod = execmod

    def __str__(self):
        return self.path

    def __repr__(self):
        return "{}:{}".format(self.name, self.path)

    def run(self):
        logger.debug("exec {} using {}".format(self.name, self.mod))
        return False