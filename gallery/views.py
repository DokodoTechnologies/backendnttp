from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class AlbumUploadView(APIView):
    def post(self, request, *args, **kwargs):
        album_title = request.data.get('album')
        files = request.FILES.getlist('imageFile')

        if not album_title or not files:
            return Response({"error": "Album name and image files are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        # 🔁 Get or create album
        album, created = Album.objects.get_or_create(title=album_title)

        # 📸 Create image objects
        images = []
        for f in files:
            image = Image(album=album, imageFile=f)
            image.save()
            images.append(image)

        return Response({
            "album": AlbumSerializer(album).data
        }, status=status.HTTP_201_CREATED)