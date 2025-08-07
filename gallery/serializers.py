from rest_framework import serializers
from .models import Album, Image
from rest_framework.pagination import PageNumberPagination

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'imageFile', 'uploadedAt']

class AlbumSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'title', 'createdAt', 'images']
    def get_images(self, obj):
        request = self.context.get('request')
        images = Image.objects.filter(album=obj).order_by('-id')

        # Manual pagination
        paginator = PageNumberPagination()
        paginator.page_size = 7
        paginated_images = paginator.paginate_queryset(images, request)

        serialized = ImageSerializer(paginated_images, many=True, context={'request': request}).data
        return {
            'count': images.count(),
            'results': serialized,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link()
        }