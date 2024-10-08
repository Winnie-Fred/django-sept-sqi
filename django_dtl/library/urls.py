from django.urls import path
from . import views

app_name = "library"

urlpatterns = [
    path("", views.home, name='home'),
    path("books/", views.book_list, name='book_list'),
    path("book_detail/<int:book_id>/", views.book_detail, name="book_detail"),
    path("create-book-no-django-form/", views.add_book_no_django_form, name="add_book_no_django_form"),
    path("create-book-with-django-form/", views.add_book_django_form, name="add_book_django_form"),
    path("create-book-manual-with-django-form/", views.add_book_manual_html_plus_django_form, name="add_book_manual_html_plus_django_form"),
    path("update-book-modelform/<int:book_pk>/", views.update_book_modelform, name="update_book_model_form"),
    path("update-book-forms-form/<int:book_pk>/", views.update_book_forms_form, name="update_book_forms_form"),
    path("confirm-delete/<int:book_id>/", views.confirm_delete, name="confirm_delete"),
    path("delete-book/<int:book_id>", views.delete_book, name="delete_book"),
]