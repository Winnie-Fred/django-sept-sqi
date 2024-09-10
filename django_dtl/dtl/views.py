from django.shortcuts import render

# Create your views here.

def new_view(request):
    context = {
        'my_name': 'Winifred Igboama'
    }
    return render(request, 'dtl/dtl_example.html', context)
