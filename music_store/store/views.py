from django.shortcuts import render

from .models import Artist, Album


# Create your views here.
def home(request):
    return render(request, "store/home.html")

def artists(request):
    all_artists = Artist.objects.order_by("-debut_year")
    context = {"artists": all_artists}
    return render(request, "store/artists.html", context)

def albums(request):
    all_albums = Album.objects.order_by("release_date")
    return render(request, "store/albums.html", {"albums": all_albums})