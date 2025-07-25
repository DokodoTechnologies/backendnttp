from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('user.urls')),
    path('api/v1/', include('gallery.urls')),  
    path('api/v1/', include('events.urls')),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)