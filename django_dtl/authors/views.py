from django.shortcuts import render

def all_authors(request):
    context = {
        'name': "Winifred"
    }
    return render(request, 'authors/all_authors.html', context)

def book_signings(request):
    return render(request, 'authors/book_signings.html')