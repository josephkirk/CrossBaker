from enums import *
from utils import readLocalFile, getScriptDir
import subprocess

#
Config = readLocalFile("config.json")
ExportSetting = readLocalFile("exportSetting.json")
Baker = ExportSetting["baker"]
BakerPath = Config.get(Baker)