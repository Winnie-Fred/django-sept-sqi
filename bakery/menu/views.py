from django.shortcuts import render

# Create your views here.
def menu(request):
    menu_items = ["bread", "sponge cake", "meatpie", "egg roll", "chicken pie", "croissants", "baguette"]
    context = {
        "menu": menu_items
    }
    return render(request, "menu/menu.html", context)