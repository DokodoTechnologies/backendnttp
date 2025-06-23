from rest_framework import serializers
from models import Events

class EventsSerializers(serializers.Serializer):
    class meta:
        model = Events
        fields = ['event_title','description','date','location']