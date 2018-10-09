#/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marmoset Baking Layer

@author: Nguyen Phi Hung

"""

import mset
import os
import json
import inspect
import sys

from CrossBaker import BakeMap, Import, ImportType, Padding
from pprint import pprint
from re import compile

# Variable
ImportType = Import.UseMeshName
MeshPath = r"D:/test/marmosetBaker"
SavePath = MeshPath
ExportPath = ""

if not MeshPath:
    print("Mesh Path not found")
    raise RuntimeError

# Method

class BakeGroup:
    def __init__(self, transform):
        self.transform = transform

    @property
    def high(self):
        return self.transform.getChildren()[1]

    @property
    def low(self):
        return self.transform.getChildren()[0]

    def addChild(self, childItem, gc=None):
        if "low" in childItem.name.lower():
            for item in childItem.getChildren():
                item.parent = self.low
        elif "high" in childItem.name.lower():
            for item in childItem.getChildren():
                item.parent = self.high
        else:
            for item in childItem.getChildren():
                if "low" in item.name.lower():
                    item.parent = self.low
                elif "high" in item.name.lower():
                    item.parent = self.high
                else:
                    if isinstance(gc, mset.TransformObject):
                        item.parent = gc
        childItem.destroy()

class Baker:
    def __init__(self):
        self.baker = mset.BakerObject()
        self.bakeMaps = {name:bakemapItem for name,bakemapItem in zip(BakeMap, self.baker.getAllMaps())}
        pprint(self.bakeMaps)
        self.groups = {}

    def toggleMapState(self, mapName, state):
        self.getMap(mapName).enabled = state

    def isMapEnabled(self, mapName):
        return self.getMap(mapName).enabled

    def getMap(self, mapName):
        self.bakeMaps.get(mapName)

    def setMapSuffix(self, mapName, suffix):
        self.bakeMaps.get(mapName).suffix = suffix

    def resetMapSuffix(self, mapName):
        self.bakeMaps.get(mapName).resetSuffix()

    def hasGroup(self, grpName):
        return grpName in self.groups

    def getGroup(self, grpName):
        return self.groups.get(grpName)

    def addGroup(self, name):
        grp = BakeGroup(self.baker.addGroup(name))
        self.groups[name] = grp
        return grp

    def setOutputSize(self, width , height):
        self.baker.outputWidth = width
        self.baker.outputHeight = height

    def setOuputPath(self, path):
        self.outputPath = path

    def setOuputPSD(self, state):
        self.outputSinglePsd = state

    def setOuputBits(self, value):
        self.outputBits = value

    def setOuputSamples(self, value):
        self.outputSamples = value

    def setIgnoreGroups(self, state):
        for map in self.bakeMaps.values():
            if hasattr(map, "ignoreGroups"):
                map.ignoreGroups = state

    def setDither(self, state):
        for map in self.bakeMaps.values():
            if hasattr(map, "dither"):
                map.dither = state

    def resetSuffixAll(self):
        for map in self.bakeMaps.values():
            map.resetSuffix()

    def useMultipleTextureSet(self, state):
        self.baker.multipleTextureSets = state

    def setPadding(self, paddingType):
        """None, Moderate, Extreme"""
        self.edgePadding = paddingType.name

    def setPaddingSize(self, paddingSize):
        self.edgePaddingSize = paddingSize

def getRegexGrp(regex, grpid, default=""):
    result = default
    try:
        result = regex.group(grpid)
    except IndexError:
        pass
    return result

if __name__ == "__main__":
    regex = ImportTypes[ImportType]
    mfiles = dict()
    files = (dict(
        name=getRegexGrp(regex.search(f), 1),
        path=os.path.join(MeshPath,f))
        for f in os.listdir(MeshPath) if regex.match(f))
    # files = (f for f in dirContents if os.path.isfile(f))

    baker = Baker()
    wrongNameGrp = mset.TransformObject("Wrong Namming")
    for mfile in files:
        if not baker.hasGroup(mfile["name"]):
            baker.addGroup(mfile["name"])
        obj = mset.importModel(mfile["path"])
        baker.getGroup(mfile["name"]).addChild(obj, wrongNameGrp)
    mset.saveScene(SavePath)