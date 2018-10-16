#/usr/bin/env python3
# -*- coding: utf-8 -*-

__appname = "CrossBaker"
__info = "Cross Baking Packages Interface"
__version = 1
__revision = 0
__state = "alpha"
__category = ["Texture"]
__author = "Nguyen Phi Hung"
__email = "hung.nguyen_a@virtuosgames.com"
__Date = 20181012

import os, stat, glob, shutil, sys, subprocess
from collections import namedtuple

# * Setup Logging
import logging as _logging
loggerLevel = _logging.DEBUG
logger = _logging.getLogger("__name__")
os.environ["CROSSBAKER_LOGGER_LEVEL"] = str(_logging.DEBUG)
_logLevel = int(os.getenv('CROSSBAKER_LOGGING_LEVEL', _logging.INFO))
if _logLevel:
	ch = _logging.StreamHandler(sys.stdout)
	ch.setLevel(_logLevel)
	formatter = _logging.Formatter('%(levelname)s:%(name)s [%(filename)s:%(lineno)d]# %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	logger.setLevel(_logLevel)

#  * Decor Methods
"""Copy from BLUR CROSS3D"""
def abstractmethod(function):
	""" The decorated function should be overridden by a software specific module.
	"""
	def newFunction(*args, **kwargs):
		# when debugging, raise an error
		msg = 'Abstract implementation has not been overridden.'
		mode = os.getenv('CROSS3D_ABSTRACTMETHOD_MODE')
		if mode == 'raise':
			raise NotImplementedError(debugObjectString(function, msg))
		elif mode == 'warn':
			logger.debug(debugObjectString(function, msg))
		return function(*args, **kwargs)
	newFunction.__name__ = function.__name__
	newFunction.__doc__ = function.__doc__
	newFunction.__dict__ = function.__dict__
	return newFunction

def debugObjectString(object, msg):
	import inspect
	# debug a module
	if inspect.ismodule(object):
		return '[%s module] :: %s' % (object.__name__, msg)

	# debug a class
	elif inspect.isclass(object):
		return '[%s.%s class] :: %s' % (object.__module__, object.__name__, msg)

	# debug an instance method
	elif inspect.ismethod(object):
		return '[%s.%s.%s method] :: %s' % (object.im_class.__module__, object.im_class.__name__, object.__name__, msg)

	# debug a function
	elif inspect.isfunction(object):
		return '[%s.%s function] :: %s' % (object.__module__, object.__name__, msg)

# * Utils method
from .utils import readLocalFile, getScriptDir, loadData, saveData, getLocalFile

def registerSymbol(name, value, ifNotFound=False):
	"""
		Used by the *adaptors* to register their own classes and functions as
		part of the crossBaker.  
	"""
	# initialize a value in the dictionary
	import crossbaker
	if ifNotFound and name in crossbaker.__dict__:
		return

	crossbaker.__dict__[name] = value

def registerBaker(name, value, ifNotFound=False):
	"""
		Used by the *adaptors* to register their own classes and functions as
		part of the crossBaker.  
	"""
	# initialize a value in the dictionary
	import crossbaker
	if ifNotFound and name in crossbaker.bakermod.__dict__:
		return

	crossbaker.bakermod.__dict__[name] = value

def _methodNames():
	"""
		get Package Name in crossbaker 
	"""
	filenames = glob.glob(os.path.split(__file__)[0] + '/*/__init__.py')
	ret = []
	for filename in filenames:
		modname = os.path.normpath(filename).split(os.path.sep)[-2]
		if (modname != 'abstract'):
			ret.append(os.path.normpath(filename).split(os.path.sep)[-2])
	return ret

def packageName(modname):
	return 'crossbaker.{}'.format(modname)

class ExportSetting(object):
	"""
	Get export setting json and wrap data to class
	"""
	__instance__ = None
	def __new__(cls, path="export_settings.json"):
		if not cls.__instance__:
			cls.__instance__ = super(ExportSetting, cls).__new__(cls)
			# cls.__instance__.__init__()
			cls.__instance__.__data = cls.getExportSetting(path)
		return cls.__instance__

	# def __init__(self):
	# 	pass

	def __call__(self, path=""):
		instance = self.__class__()
		if os.path.exists(path):
			instance.__data = cls.getExportSetting(path)
		for key, value in instance.__data.items():
			if key == "OutputSize":
				instance.outputSize = Size(*instance.__data.get("OutputSize", [2048, 2048]))
				continue
			instance.__dict__[key.lower()[0] + key[1:]] = value
		return instance

	def init(self):
		return self()

	def get(self, attrname):
		return self().__data.get(attrname)

	@staticmethod
	def getExportSetting(path):
		try:
			# read Path from relative
			_exportSettings = readLocalFile(path)
		except:
			# read Path from absolute
			try:
				_exportSettings = loadData(path)
			except:
				_exportSettings = {}
		return _exportSettings

class Bakers(object):
	"""
	Class return available baker in system using path set in config.json
	"""
	__instance__ = None
	def __new__(cls, path="config.json"):

		if not cls.__instance__:
			cls.__instance__ = super(Bakers, cls).__new__(cls)
			# cls.__instance__.__init__()
			cls.__instance__.__allApps = cls.getConfig(path)
			cls.__instance__.__availApps = {}

		return cls.__instance__

	def __call__(self, path=""):
		instance = self.__class__()
		if os.path.exists(path):
			instance.__data = self.getConfig(path)
		import crossbaker
		for bakername, bakerpath in instance.__allApps.items():
			if not os.path.exists(bakerpath):
				continue
			if bakername == "pythonexternal":
				crossbaker.externalPython = bakername
				continue
			elif bakername == "photoshop":
				crossbaker.photoshop = bakername
				continue
			logger.debug('Baker Application: "{}" found.'.format(bakername.capitalize()))
			instance.__availApps[bakername] = BakerApp(bakername, bakerpath)
		# Attemp to aquire execution module for baker application
		for bakerapp in instance.__availApps:
			if bakerapp in crossbaker.bakermod.__dict__:
				instance.__availApps[bakerapp].mod = crossbaker.bakermod.__dict__[bakerapp]
		# register Baker as class Attribute
		instance.__dict__.update(instance.__availApps)
		return instance

	def __iter__(self):
		self.__bakerid = 0
		return self()

	def __next__(self):
		if self.__bakerid >= len(self.__availApps):
			raise StopIteration
		baker = list(self.__availApps.values())[self.__bakerid]
		self.__bakerid += 1
		return baker

	# def __init__(self):
	# 	pass

	def init(self):
		return self()

	def current(self):
		return self().get(ExportSetting().baker)

	def run(self):
		return self.current().run()

	def get(self, bakerName):
		return self().__availApps.get(bakerName)

	def count(self):
		return len(self().__availApps.keys())

	def countAll(self):
		return len(self().__allApps.keys())

	@staticmethod
	def getConfig(path):
		try:
			# read Path from relative
			_config = readLocalFile(path)
		except:
			# read Path from absolute
			try:
				_config = loadData(path)
			except:
				_config = {}
		return _config

def init():
	for modname in _methodNames():
		pckg = packageName(modname)
		# Attempt to import and init this modname.
		try:
			__import__(pckg)
		except ImportError:
			continue

		mod = sys.modules[pckg]
		try:
			mod.init()
			logger.debug('The module "{}" initialized successfully.'.format(modname))
			# The module successfully initalized no need to try any other modules.
			break
		except:
			continue
	
	## Register Setting
	exportSetting.init()
	bakers.init()
# ----- #

## Init Enum and BaseClass
from .enums import \
    Import, \
    ImportTypes, \
    Padding, \
    BakeMap

from .libs.classes import \
	Size, \
	BakerApp, \
	ImageApp

# * Init crossbaker
## Setup configuration
Config = "config/config.json"
Setting = "config/export_settings.json"
TempPath = os.path.join(os.getenv("LOCALAPPDATA"), __appname)
UserConfig = os.path.normpath(os.path.join(TempPath, Config))
UserSetting = os.path.normpath(os.path.join(TempPath, Setting))

Clean = False
if Clean:
	def remove_readonly(func, path, _):
		"Clear the readonly bit and reattempt the removal"
		os.chmod(path, stat.S_IWRITE)
		func(path)
	shutil.rmtree(TempPath, onerror=remove_readonly)

if not os.path.isdir(TempPath):
	os.mkdir(TempPath)
if not os.path.isdir(TempPath+"/config"):
	shutil.copytree(getLocalFile("config"), TempPath+"/config")

## Init Setting
logger.debug(getScriptDir())
exportSetting =  ExportSetting(UserSetting)
bakers = Bakers(UserConfig)
init()