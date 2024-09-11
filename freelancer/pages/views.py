from django.shortcuts import render


services_offered = {
    "data analysis": 900000,
    "web development": 600000,
    "app development": 400000,
    "digital marketing": 7000000,
}

# Create your views here.
def services(request):
    return render(request, "pages/services.html", {'services': services_offered})

def testimonials(request):
    client_testimonials = {
        "John Smith": "The service exceeded my expectations. The team was professional and delivered outstanding results.",
        "Emily Johnson": "I am extremely satisfied with the work. They truly understood our needs and provided the perfect solution.",
        "Mr. Emmanuel": "Fantastic experience! The project was completed on time, and the results were beyond what we had hoped for.",
        "Sophia Davis": "Their attention to detail and customer service were top-notch. We will definitely be working with them again.",
        "Liam Wilson": "Highly recommend! They turned a complex problem into a simple, elegant solution. Couldn't be happier.", 
    }

    ratings =  [3.0, 4.0, 3.5, 5.0, 1.0]

    context = {
        'testimonials': client_testimonials,
        'ratings': ratings
    }
    return render(request, "pages/testimonials.html", context)

def case_studies(request):
    return render(request, "pages/case-studies.html")

def blog(request):
    return render(request, "pages/blog.html")

def pricing(request):
    context = {'services': services_offered}
    return render(request, "pages/pricing.html", context)