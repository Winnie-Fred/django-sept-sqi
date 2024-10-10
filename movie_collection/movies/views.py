from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Movie
from .forms import MovieForm

# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/movie-list.html", {"movies": movies})

def create_movie(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("movies:movie_list")

    context = {"form": form}
    return render(request, "movies/create-movie.html", context)

def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, "movies/movie-detail.html", {"movie": movie})

def edit_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = MovieForm(instance=movie)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect(reverse("movies:movie_detail", args=[movie_pk]))
    context = {"form": form, "movie": movie}
    return render(request, "movies/edit-movie.html", context)

def confirm_delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return render(request, "movies/confirm-delete.html", {"movie": movie})

def delete_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "POST":
        movie.delete()
        return redirect("movies:movie_list")
    return redirect("movies:movie_detail")
