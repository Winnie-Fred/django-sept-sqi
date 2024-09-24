from django.shortcuts import render, get_object_or_404

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

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, "store/artist_detail.html", {"artist": artist})
