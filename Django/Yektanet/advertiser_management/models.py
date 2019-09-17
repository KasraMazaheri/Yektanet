from django.db import models

class BaseAdvertising(models.Model):
    clicks = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    def getClicks(self):
        return self.clicks
    def getViews(self):
        return self.views
    def incClicks(self):
        pass
    def incViews(self):
        pass

class Advertiser(BaseAdvertising):
    name = models.CharField(max_length = 200)
    def getTotalClicks():
        #to be added ...
        return 0
    def incClicks(self):
        self.clicks += 1
        self.save()
    def incViews(self):
        self.views += 1
        self.save()


class Ad(BaseAdvertising):
    title = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    _advertiser = models.ForeignKey(Advertiser, on_delete = models.CASCADE)
    def incClicks(self):
        self.clicks += 1
        self._advertiser.incClicks()
        self.save()
    def incViews(self):
        self.views += 1
        self._advertiser.incViews()
        self.save()
