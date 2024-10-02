from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, "book/book-list.html", {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    context = {"book": book, "reviews": reviews, "form": form}
    return render(request, "book/book-detail.html", context)

def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews:book_list")
    context = {"book": book, "reviews": reviews, "form": form}
    return render(request, "book/book-detail.html", context)
        
        
    
    