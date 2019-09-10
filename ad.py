from advertiser import *
class Ad(BaseAdvertising):
	'This class is meant to represent an ad.'
	def __init__(self, ID, TITLE, IMGURL, LINK, ADVERTISER):
		self._id = ID
		self.__title = TITLE
		self.__imgUrl = IMGURL
		self.__link = LINK
		self.__advertiser = ADVERTISER
		self._clicks = self._views = 0
	def getTitle(self):
		return self.__title
	def setTitle(self, TITLE):
		self.__title = TITLE
	def getImgUrl(self):
		return self.__imgUrl
	def setImgUrl(self, IMGURL):
		self.__imgUrl = IMGURL
	def getLink(self):
		return self.__link
	def setLink(self, LINK):
		self.__link = LINK
	def setAdvertiser(self, ADVERTISER):
		self.__advertiser = ADVERTISER
	def incClicks(self):
		self._clicks += 1
		self.__advertiser.incClicks()
	def incViews(self):
		self._views += 1
		self.__advertiser.incViews()
	def describeMe(self):
		return Ad.__doc__
