from django.contrib import admin
from .models import Album, Image
from django.utils.html import mark_safe
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.imagefile:
            return mark_safe(f'<img src="{obj.imagefile.url}" width="150" height="auto" />')
        return "No image"

    image_preview.short_description = "Preview"

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInline] # Inlines will typically get their own tab automatically in Jazzmin.

