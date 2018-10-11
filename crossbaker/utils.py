#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Utilities

@author: Nguyen Phi Hung

"""
from math import floor
import inspect
import json
import os
import win32net
import pprint
# import os
def void(*args, **kws):
    pass

def infoprint(mod):
    print(type(mod))
    pprint(dir(mod))

def readLocalFile(fileName):
    with open(getLocalFile(fileName)) as read_file:
        data = json.load(read_file)
    return data

def getScriptDir():
    return os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def saveData(data, filePath):
    with open(filePath, 'w') as write_file:
        json.dump(data, write_file, indent=4, sort_keys=True)

def loadData(filePath):
    with open(filePath, 'r') as read_file:
        return json.load(read_file)

def getLocalFile(fileName):
    return os.path.normpath(os.path.join(getScriptDir(), fileName))

def saveLocalData(data, fileName, ext="json"):
    saveData(data, os.path.join(getScriptDir(),"{}.{}".format(fileName, ext)))

def loadLocalData(fileName, ext="json"):
    return loadData(os.path.join(getScriptDir(),"{}.{}".format(fileName, ext)))

def getUserName():
    userData = os.environ["USERNAME"]
    try:
        userData = win32net.NetUserGetInfo("virtuosgames.com", os.environ["USERNAME"], 2)['full_name']
    except: 
        try:
            userData = win32net.NetUserGetInfo("virtuos-sparx.com", os.environ["USERNAME"], 2)['full_name']
        except:
            pass
    print(userData)
    return userData