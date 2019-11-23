from rest_framework import serializers
from .models import Advertiser, Ad

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['name']

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title', 'image', 'link', 'advertiser', 'approved']
