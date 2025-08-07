from django.shortcuts import render
from rest_framework import viewsets
from .models import Events
from .serializers import *
# Create your views here.
class EventsViewset(viewsets.ModelViewSet):
    serializer_class = EventsSerializers
    def get_queryset(self):
        return Events.objects.filter(news_url__isnull=True)
class NewsViewset(viewsets.ModelViewSet):
    serializer_class = NewsSerializers
    def get_queryset(self):
        return Events.objects.filter(news_url__isnull=False)