from django.urls import path

from . import views

app_name = "reviews"

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("book-detail/<int:pk>/", views.book_detail, name="book_detail"),
    path("create-review/<int:book_id>/", views.create_review, name="create_review"),
]