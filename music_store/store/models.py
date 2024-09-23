from django.db import models

from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

def validate_year(value):
    current_year = timezone.now().year
    if value < 1800 or value > current_year:
        raise ValidationError(f"{value} is an incorrect year. Choose between 1800 and {current_year}")

class Artist(models.Model):
    name = models.CharField(max_length=255)
    debut_year = models.IntegerField(validators=[validate_year])
    picture = models.ImageField(upload_to="artists_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to="album_cover_pages/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"