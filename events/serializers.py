from rest_framework import serializers
from .models import Events

class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_title','description','date','location','image']


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_title','description','date','location','image','news_url']