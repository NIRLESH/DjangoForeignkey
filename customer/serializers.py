from rest_framework import serializers
from .models import Industry, Advertiser 
 
class IndustrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Industry 
        fields = ['id', 'name', 'description']


class AdvertiserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertiser 
        fields = ['id', 'name', 'description','mobileno']