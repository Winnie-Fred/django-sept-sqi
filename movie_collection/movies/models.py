from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class GenreChoices(models.TextChoices):
    ACTION = 'AC', 'Action'
    DRAMA = 'DR', 'Drama'
    COMEDY = 'CO', 'Comedy'
    HORROR = 'HO', 'Horror'
    ROMANCE = 'RO', 'Romance'
    SCIFI = 'SF', 'Science Fiction'
    FANTASY = 'FA', 'Fantasy'
    DOCUMENTARY = 'DO', 'Documentary'
    THRILLER = 'TH', 'Thriller'

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(choices=GenreChoices, default=GenreChoices.ACTION, max_length=2)
    description = models.TextField()
    poster = models.ImageField(upload_to="posters/", blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

