from django.shortcuts import render

from .models import Author
from library.models import Book

from datetime import datetime

def all_authors(request):
    context = {
        'name': "Winifred"
    }
    return render(request, 'authors/all_authors.html', context)

def book_signings(request):
    return render(request, 'authors/book_signings.html')

def authors_books(request):
    all_authors = Author.objects.all()
    all_books = Book.objects.all()
    year_2000 = datetime(2000, 1, 1)
    old_authors = all_authors.filter(birth_date__lt=year_2000)
    # try:
    #     agatha = Author.objects.get(first_name="Agathaaaaaaa", last_name="Christie")
    # except Author.DoesNotExist:
    #     agatha = None
    agatha = Author.objects.get(first_name="Agatha", last_name="Christie")


    # agatha = Author.objects.filter(first_name="Agathaaaaaaa", last_name="Christie").first()
    
    roger_ackroyd_book = Book.objects.get(title="The murder of Roger Ackroyd", author=agatha)
    # old_authors = Author.objects.filter(birth_date__lt=year_2000)
    authors_with_books = Author.objects.exclude(book__isnull=True)
    sorted_authors = Author.objects.order_by('first_name')
    recently_published = Book.objects.order_by("-published_on")



    context = {
        'all_the_authors': all_authors,
        'all_the_books': all_books,
        "roger_ackroyd": roger_ackroyd_book,
        "old_authors": old_authors,
        "authors_with_books": authors_with_books,
        "sorted_authors": sorted_authors,
        "recently_published": recently_published,
    }
    return render(request, "authors/authors_books.html", context)