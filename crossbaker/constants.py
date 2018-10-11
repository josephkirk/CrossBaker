#/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple

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