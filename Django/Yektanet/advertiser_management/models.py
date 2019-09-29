from django.db import models

class Advertiser(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class Ad(models.Model):
    title = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    link = models.CharField(max_length = 200)
    advertiser = models.ForeignKey(Advertiser, on_delete = models.CASCADE)
    approved = models.IntegerField(default = 0)
    def __str__(self):
        return self.title

class Click(models.Model):
    ip = models.CharField(max_length = 200)
    time = models.DateTimeField(auto_now = True)
    ad = models.ForeignKey(Ad, on_delete = models.CASCADE)
    def get_time(self):
        return self.time.hour

class View(models.Model):
    ip = models.CharField(max_length = 200)
    time = models.DateTimeField(auto_now = True)
    ad = models.ForeignKey(Ad, on_delete = models.CASCADE)
    def get_time(self):
        return self.time.hour








    
