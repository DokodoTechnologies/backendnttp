from django.db import models

# Create your models here.
class Events(models.Model):
    event_title = models.CharField(max_length=255, verbose_name="Event Title")
    data = models.DateField(verbose_name="Event Date")
    location= models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.event_title} - {self.event_date.strftime('%Y-%m-%d')}"