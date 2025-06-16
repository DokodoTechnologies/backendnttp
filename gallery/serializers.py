from rest_framework import serializers
from .models import Album, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'imageFile', 'uploadedAt']

class AlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'createdAt', 'images']

class AlbumUploadSerializer(serializers.Serializer):
    album = serializers.CharField(max_length=255)
    imageFile = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )

    def create(self, validated_data):
        title = validated_data.get('album')
        images = validated_data.get('imageFile')

        # Create album
        album = Album.objects.create(title=title)

        # Create images
        for image in images:
            Image.objects.create(album=album, imageFile=image)

        return album
