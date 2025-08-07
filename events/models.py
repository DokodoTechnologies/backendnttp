from django.db import models

# Create your models here.
class Events(models.Model):
    event_title = models.CharField(max_length=255, verbose_name="Event Title")
    date = models.DateField(verbose_name="Event Date", blank= True,null = True)
    location= models.CharField(max_length=255, blank= True,null = True)
    description = models.CharField(max_length=255, blank= True,null = True)
    image = models.ImageField(upload_to='event_images/', blank= True,null = True)
    news_url = models.URLField(max_length= 255, blank= True,null = True)

    class Meta:
        verbose_name = "News and Event"
        verbose_name_plural = "News and Events"

    def __str__(self):
        return f"{self.event_title} - {self.date.strftime('%Y-%m-%d')}"