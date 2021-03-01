from django.shortcuts import render
from .models import Industry, Advertiser
from rest_framework import generics
from .serializers import IndustrySerializer, AdvertiserSerializer


class IndustryCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Industry
	queryset = Industry.objects.all(),
	serializer_class = IndustrySerializer


class IndustryList(generics.ListAPIView):
    # API endpoint that allows Industry to be viewed.
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class IndustryDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Industry by pk.
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class IndustryUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Industry record to be updated.
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class IndustryDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Industry record to be deleted.
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class AdvertiserCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Industry
	queryset = Advertiser.objects.all(),
	serializer_class = AdvertiserSerializer


class AdvertiserList(generics.ListAPIView):
    # API endpoint that allows Industry to be viewed.
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

class AdvertiserDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Industry by pk.
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer