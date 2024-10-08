from django.urls import path

from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("artists/", views.artists, name="artists"),
    path("albums/", views.albums, name="albums"),
    path("artist-detail/<int:artist_id>/", views.artist_detail, name="artist_detail"),
]