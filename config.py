import configparser
from urllib.request import urlopen

import requests as requests


class Config:
	def __init__(self, path: str):
		self.ini = path

	def readConfig(self) -> dict:
		""" Read config, check for errors and store values

		:return: config as dict
		"""
		# Read config file
		config = configparser.ConfigParser()
		if "http" not in self.ini:
			config.read(self.ini)
		else:
			response = requests.get(self.ini)
			if response.status_code == 200:
				ini = f"{urlopen(self.ini).read()}"[2:-1].replace("\\n", "\n")
				config.read_string(ini)

			else:
				config = False

		# Return
		return self.matchConfig(config)

	def matchConfig(self, ini: dict):

		matched = {}
		for entity, settings in ini.items():
			matched[entity] = {}
			if entity == "formatter_simple" or entity == "formatter_verbose":
				matched[entity] = settings
			else:
				for key, value in settings.items():
					if isInteger(value):
						matched[entity][key] = int(value)
					elif isFloat(value):
						matched[entity][key] = float(value)
					elif isBoolean(value) is True and not None:
						matched[entity][key] = True
					elif isBoolean(value) is False and not None:
						matched[entity][key] = False
					else:
						matched[entity][key] = str(value)

		return matched

def isFloat(i):
	try:
		float(i)
		return True
	except:
		return False

def isInteger(i):
	try:
		int(i)
		return True
	except:
		return False

def isBoolean(i):
	match i:
		case "True" | "true" | "Yes" | "yes":
			return True
		case "False" | "false" | "No" | "no":
			return False
		case _ :
			return None
