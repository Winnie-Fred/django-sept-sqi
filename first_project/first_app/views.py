from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>My first Django project</h1>")


def about(request):
    return HttpResponse("<h3>About Page</h3>")

# 1. Create a new folder
# 2. In the new folder, create a virtual environment
# 3. Activate the virtual environment
# 4. Install django
# 5. Create a django project, call it whatever you like
# 6. Start the development server
