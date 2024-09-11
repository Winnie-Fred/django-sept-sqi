from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo_view_one(request):
    return HttpResponse("Demo view one")

def demo_view_two(request):
    return HttpResponse("Demo view two")
