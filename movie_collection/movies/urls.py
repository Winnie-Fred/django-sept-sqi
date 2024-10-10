from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("list-movies/", views.movie_list, name="movie_list"),
    path("create-movie/", views.create_movie, name="create_movie"),
    path("movie/<int:movie_pk>/", views.movie_detail, name="movie_detail"),
    path("edit-movie/<int:movie_pk>/", views.edit_movie, name="edit_movie"),
    path("confirm-delete/<int:movie_pk>/", views.confirm_delete, name="confirm_delete"),
    path("delete-movie/<int:movie_pk>/", views.delete_movie, name="delete_movie"),
]