from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def subscribe(request):
    return render(request, "newsletter/subscribe.html")