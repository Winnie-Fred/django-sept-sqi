from django.shortcuts import render

def home(request):
    return render(request, 'library/home.html')

def book_list(request):
    return render(request, 'library/book_list.html')