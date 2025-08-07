from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventsViewset, NewsViewset

router = DefaultRouter()
router.register(r'events', EventsViewset, basename='events')
router.register(r'news', NewsViewset, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]
