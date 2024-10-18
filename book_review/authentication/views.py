from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def sign_up(request):
    form = UserCreationForm()
    if request.method == "POST":
        print(request.POST)
        print(form)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("authentication:login")
    context = {"form": form}
    return render(request, "authentication/sign-up.html", context)