from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account created successfully")
            form.save()
            return redirect("authentication:login")
    return render(request, "authentication/sign-up.html", {"form":form})