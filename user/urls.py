from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]
