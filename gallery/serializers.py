# serializers.py

from rest_framework import serializers
from .models import Album, Image

from .models import Album, Image
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'createdAt']

class ImageSerializer(serializers.ModelSerializer):
    album = serializers.CharField(write_only=True)  # incoming string title
    album_info = serializers.SerializerMethodField(read_only=True) 

    class Meta:
        model = Image
        fields = ['id', 'title', 'imageFile', 'album', 'uploadedAt','album_info']
        read_only_fields = ['id', 'uploadedAt']
    def create(self, validated_data):
        album_title = validated_data.pop('album')
        album, _ = Album.objects.get_or_create(title=album_title)
        image = Image.objects.create(album=album, **validated_data)
        return image

    def get_album_info(self, obj):
        return {
            "id": obj.album.id,
            "title": obj.album.title
        }