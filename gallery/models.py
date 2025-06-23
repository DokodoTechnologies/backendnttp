from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Image(models.Model):
    album = models.ForeignKey(Album, related_name='images', on_delete=models.CASCADE)
    imageFile = models.ImageField(upload_to='gallery_images/')
    uploadedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.imageFile.name
