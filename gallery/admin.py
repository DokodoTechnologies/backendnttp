from django.contrib import admin
from .models import Album, Image

class ImageInline(admin.TabularInline):  # You can also use StackedInline
    model = Image
    extra = 1  # Number of empty image forms shown
    fields = ['imageFile']
    max_num = 10  # Optional: limit the number of images
    # You can also use: readonly_fields = ['imageFile'] if needed

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImageInline]
