from django.db import models

from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField()
    published_on = models.DateField()
    cover_page = models.ImageField(upload_to="book_cover_pages/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.author}"