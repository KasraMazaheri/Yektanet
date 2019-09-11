# ItonE
class BaseAdvertising:
	'This class is the base of our other classes.'
	def __init__(self):
		print("Holy shit")
	def getClicks(self):
		return self._clicks
	def getViews(self):
		return self._views
	def incClicks(self):
		pass
	def incViews(self):
		pass
	def describeMe(self):
		return BaseAdvertising.__doc__
