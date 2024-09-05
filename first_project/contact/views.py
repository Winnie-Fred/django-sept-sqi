from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def email(request):
    return render(request, "contact/email.html")

def phone(request):
    return render(request, "contact/phone.html")