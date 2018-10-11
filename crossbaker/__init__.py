from utils import readLocalFile, getScriptDir
import subprocess
import glob
import os
import sys

# Init Enum and Constants
from enums import \
    Import, \
    ImportTypes, \
    Padding, \
    BakeMap

# Init Setting
Config = readLocalFile("config.json")
ExportSetting = readLocalFile("exportSetting.json")
Baker = ExportSetting["baker"]
BakerPath = Config.get(Baker)

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
# init crossbaker
