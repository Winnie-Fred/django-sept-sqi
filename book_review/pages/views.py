from django.shortcuts import render, get_object_or_404

from review.models import Book, Review

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

def library(request):
    return render(request, "pages/library.html")

def books(request):
    all_books = Book.objects.all()
    return render(request, "pages/books.html", {"books": all_books})

def book_detail(request, book_id):
    book =  get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    context = {
        "book": book,
        "reviews": reviews,
    }
    return render(request, "pages/book_detail.html", context)



