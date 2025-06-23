from django.shortcuts import render
from rest_framework import viewsets
from models import Events
from serializers import EventsSerializers
# Create your views here.
class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializers