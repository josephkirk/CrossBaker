#/usr/bin/env python3
# -*- coding: utf-8 -*-
from crossBaker import BakeMap, abstractMethod

class BakeGroup:
    def __init__(self):
        pass

    @property
    def high(self):
        pass

    @property
    def low(self):
        pass

    def addChild(self, childItem, gc=None):
        pass

class Baker:
    def __init__(self):
        self.baker = None
        self.bakeMaps = BakeMap
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
        grp = BakeGroup()
        self.groups[name] = grp
        return grp

    def setOutputSize(self, width , height):
        self.baker.outputWidth = width
        self.baker.outputHeight = height

    def setOuputPath(self, path):
        self.baker.outputPath = path

    def setOuputPSD(self, state):
        self.baker.outputSinglePsd = state

    def setOuputBits(self, value):
        self.baker.outputBits = value

    def setOuputSamples(self, value):
        self.baker.outputSamples = value

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
        self.baker.edgePadding = paddingType.name

    def setPaddingSize(self, paddingSize):
        self.baker.edgePaddingSize = paddingSize