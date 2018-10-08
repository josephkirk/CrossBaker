import mset
import os
import sys
from regex import match

importPath = ""

files = (f for f in os.listDir() if os.path.isfile(f))
regex = r"\w*_(low|high)_?\w*"

objs = mset.importModel(importPath)

baker = mset.BakerObject()
