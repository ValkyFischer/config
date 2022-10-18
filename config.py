import configparser

class Config:
	def __init__(self, path: str):
		self.ini = path

	def readConfig(self) -> dict:
		""" Read config, check for errors and store values

		:param ini: Path to config.ini
		:return: config as dict
		"""
		# Read config
		config = configparser.ConfigParser()
		config.read(self.ini)
		# Return
		return config