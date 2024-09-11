from django.shortcuts import render

# Create your views here.

def new_view(request):
    context = {
        'my_name': 'Winifred Igboama',
        'is_dark': True,
        'students': ["Abdur-Rahman", "Joseph", "Dr. Gafar", "Sam", "Gbemisola", "Emmanuel", "Solomon", "Dr. Shina"]
    }
    return render(request, 'dtl/dtl_example.html', context)
