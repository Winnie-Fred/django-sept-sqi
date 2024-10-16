from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("library/", views.library, name="library"),
    path("books/", views.books, name="books"),
    path("book-detail/<int:book_id>/", views.book_detail, name="book_detail"),

]