from django.shortcuts import render, redirect, get_object_or_404

from authors.models import Author
from .models import Book
from .forms import BookForm, BookManualForm

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


def add_book_django_form(request):
    form = BookForm()
    if request.method == "POST":
        print(request.POST)
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("library:book_list")

    context = {
        "add_book_form": form,
    }

    return render(request, "library/add_book_with_django_form.html", context)

def add_book_manual_html_plus_django_form(request):
    form = BookManualForm()
    if request.method == "POST":
        form = BookManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get("title")
            author = cleaned_data.get("author")
            number_of_pages = cleaned_data.get("number_of_pages")
            published_on = cleaned_data.get("published_on")
            cover_page = cleaned_data.get("cover_page")
            Book.objects.create(title=title, author=author, number_of_pages=number_of_pages, published_on=published_on, cover_page=cover_page)
            return redirect("library:book_list")

    context = {
        "manual_book_form": form, 
    }
    return render(request, "library/add_book_with_manual_html_form.html", context)


def update_book_modelform(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("library:book_list")
        
    context = {
        "form": form,
        "book": book,
    }
    return render(request, "library/update-book-modelform.html", context)


def update_book_forms_form(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    initial_data = {
        "title": book.title,
        "author": book.author,
        "number_of_pages": book.number_of_pages,
        "published_on": book.published_on,
        "cover_page": book.cover_page,
    }
    form = BookManualForm(initial=initial_data)
    if request.method == "POST":
        form = BookManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get("title")
            author = cleaned_data.get("author")
            number_of_pages = cleaned_data.get("number_of_pages")
            published_on = cleaned_data.get("published_on")
            cover_page = cleaned_data.get("cover_page")
            book.title = title
            book.author = author
            book.number_of_pages = number_of_pages
            book.published_on = published_on
            if cover_page:
                book.cover_page = cover_page
            book.save()
            return redirect("library:book_list")

    context = {
        "form": form,
        "book": book,
    }
    return render(request, "library/update-book-forms-form.html", context)


def confirm_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "library/confirm-delete.html", {"book": book})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
    return redirect("library:book_list")
    

