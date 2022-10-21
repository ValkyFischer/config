import configparser
from urllib.request import urlopen

import requests as requests


class Config:
	def __init__(self, path: str):
		self.ini = path

	def readConfig(self) -> dict:
		""" Read config, check for errors and store values

		:param ini: Path to config.ini
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
		return config