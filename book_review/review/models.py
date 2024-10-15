from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Models):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    year_of_birth = models.DateField()

class GenreChoices(models.TextChoices):
    FANTASY = "FNT", "Fantasy"
    SCI_FI = "SCIFI", "Science Fiction"
    MYSTERY_THRILLER = "MYST_THRILL", "Mystery/Thriller"
    ROMANCE = "ROM", "Romance" 


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(choices=GenreChoices, default=GenreChoices.MYSTERY_THRILLER)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to="book_cover_images/")
    isbn = models.CharField(max_length=255)
    number_of_pages = models.PositiveIntegerField()

def validate_rating(rating):
    if rating < 1 or rating > 5:
        raise ValidationError("Rating must be between 1 and 5")

class Review(models.Model):
    review = models.TextField()
    rating = models.PositiveIntegerField(validators=[validate_rating])
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateField(auto_now_add=True)
