from django import forms

from .models import Book
from authors.models import Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'number_of_pages','published_on','cover_page']


class BookManualForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    number_of_pages = forms.IntegerField()
    published_on = forms.DateTimeField()
    cover_page = forms.ImageField(required=False)