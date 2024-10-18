from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from review.models import Book

from .forms import ReviewForm

def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Review added successfully")
            # return redirect(reverse("pages:book_detail", args=[book_id]))
            return redirect("pages:book_detail", book_id)
    context = {"form": form, "book": book}
    return render(request, "review/create-review.html", context)