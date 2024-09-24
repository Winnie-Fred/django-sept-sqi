from django.shortcuts import render, redirect, get_object_or_404

from authors.models import Author
from .models import Book

def home(request):
    return render(request, 'library/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {"books": books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "library/book_detail.html", {"book": book})

def add_book_no_django_form(request):
    authors = Author.objects.all()
    context = {
        "authors": authors,
    }
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        number_of_pages = request.POST.get("number_of_pages")
        published_on = request.POST.get("published_on")
        cover_page = request.FILES.get("cover_page")

        if not title or not author_id or not number_of_pages or not published_on:
            error = "Title, author, number_of_pages, published_on are all required"
            context.update({
                "error": error
            })
            return render(request, "library/add_book_no_django_form.html", context)

        try:
            number_of_pages = int(number_of_pages)
        except ValueError:
            error = "Number of pages must be a number"
            context.update({
                "error": error
            })
            return render(request, "library/add_book_no_django_form.html", context)
        
        try:
            author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            error = "That author does not exist"
            context.update({
                "error": error
            })
            return render(request, "library/add_book_no_django_form.html", context)
        

        cover_page = cover_page if cover_page else None

        Book.objects.create(title=title, author=author, number_of_pages=number_of_pages, published_on=published_on, cover_page=cover_page)
        return redirect("library:book_list")

    return render(request, "library/add_book_no_django_form.html", context)