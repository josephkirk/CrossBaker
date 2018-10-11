#/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CrossBaker Initialize

@author: Nguyen Phi Hung

"""
import subprocess
import glob
import os
import sys
from collections import namedtuple

# Setup Logging
import logging as _logging
loggerLevel = _logging.DEBUG
logger = _logging.getLogger("__name__")
_logLevel = int(os.getenv('CROSSBAKER_LOGGING_LEVEL', _logging.INFO))
if _logLevel:
	ch = _logging.StreamHandler(sys.stdout)
	ch.setLevel(_logLevel)
	formatter = _logging.Formatter('%(levelname)s:%(name)s [%(filename)s:%(lineno)d]# %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)
	logger.setLevel(_logLevel)

# Decor Methods
def abstractmethod(function):
	""" The decorated function should be overridden by a software specific module.
	
	Depending on the state of the environment variable "CROSS3D_ABSTRACT_MODE" is set to 
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

# utils method
from .utils import readLocalFile, getScriptDir, loadData, saveData

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
		try:
			# read Path from relative
			_exportSettings = readLocalFile(path)
		except:
			# read Path from absolute
			try:
				_exportSettings = loadData(path)
			except:
				_exportSettings = {}
		if not cls.__instance__:
			cls.__instance__ = super(ExportSetting, cls).__new__(cls)
			cls.__instance__._data = _exportSettings
		for key, value in _exportSettings.items():
			if key == "OutputSize":
				cls.__instance__.outputSize = Size(*_exportSettings.get("OutputSize", [2048, 2048]))
				continue
			cls.__instance__.__dict__[key.lower()[0] + key[1:]] = value
		return cls.__instance__

	@classmethod
	def getSetting(cls, attrname):
		return cls.__instance__._data.get(attrname)


class Bakers(object):
	"""
	Class return available baker in system using path set in config.json
	"""
	__instance__ = None
	def __new__(cls, path="config.json"):
		try:
			# read Path from relative
			_config = readLocalFile(path)
		except:
			# read Path from absolute
			try:
				_config = loadData(path)
			except:
				_config = {}
		if not cls.__instance__:
			cls.__instance__ = super(Bakers, cls).__new__(cls)
			cls.__instance__.__allApps = _config
			cls.__instance__.__availApps = {}

		import crossbaker
		for bakername, bakerpath in _config.items():
			if bakername == "pythonexternal":
				crossbaker.externalPython = bakername
				continue
			if os.path.exists(bakerpath):
				logger.debug('Baker Application: "{}" found.'.format(bakername.capitalize()))
				cls.__instance__.__availApps[bakername] = BakerApp(bakername, bakerpath)
		# Attemp to aquire execution module for baker application
		for bakerapp in cls.__instance__.__availApps:
			if bakerapp in crossbaker.bakermod.__dict__:
				cls.__instance__.__availApps[bakerapp].mod = crossbaker.bakermod.__dict__[bakerapp]
		# register Baker as class Attribute
		cls.__instance__.__dict__.update(cls.__instance__.__availApps)
		return cls.__instance__

	@classmethod
	def current(cls):
		return cls.__instance__.get(ExportSetting().baker)

	@classmethod
	def get(cls, bakerName):
		return cls.__instance__.__availApps.get(bakerName)

	@classmethod
	def count(cls):
		return len(cls.__instance__.__availApps.keys())

	@classmethod
	def countAll(cls):
		return len(cls.__instance__.__allApps.keys())

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

	exportSetting()
	bakers()
# ----- #

# ***Init crossbaker***
os.environ["CROSSBAKER_LOGGER_LEVEL"] = str(_logging.DEBUG)
## Init Setting
logger.debug(getScriptDir())

## Init Enum and Constants
from .enums import \
    Import, \
    ImportTypes, \
    Padding, \
    BakeMap

from .constants import \
	Size, \
	BakerApp
##

## Register internalMethod
exportSetting = ExportSetting
bakers = Bakers

##
init()