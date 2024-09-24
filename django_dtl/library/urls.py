from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("", views.home, name='home'),
    path("books/", views.book_list, name='book_list'),
    path("book_detail/<int:book_id>/", views.book_detail, name="book_detail"),
    path("create-book-no-django-form/", views.add_book_no_django_form, name="add_book_no_django_form"),
]