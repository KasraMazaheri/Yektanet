from base_model import *
class Advertiser(BaseAdvertising):
	'This calss is meant to represent an advertiser'
	totalClicks = 0
	def __init__(self, ID, NAME):
		self._id = ID
		self.__name = NAME
		self._clicks = self._views = 0
	def getName(self):
		return self.__name
	def setName(self, NAME):
		self.__name = NAME
	def getTotalClicks():
		return Advertiser.totalClicks
	def incClicks(self):
		self._clicks += 1
		Advertiser.totalClicks += 1
	def incViews(self):
		self._views += 1
	def describeMe(self):
		return Advertiser.__doc__
	def help():
		return """Here's a short description for each field of this class :
		id: The id of this advertiser.
		name: The name of the advertiser.
		totalClicks: The total number of clicks that were made.
		clicks: The number of clicks that were made on this advertiser's ads.
		views: The number of times one of this advertiser's ads was viewed."""
