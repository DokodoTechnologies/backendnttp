from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'image', ImageViewSet, basename='image')
router.register(r'album',AlbumViewSet, basename='album')

urlpatterns = [
    path('', include(router.urls)),
    path('upload-album/', AlbumUploadView.as_view(), name='upload-album'),
]
