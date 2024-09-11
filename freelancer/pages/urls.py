from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("services-offered/", views.services, name="services"),
    path("client-testimonials/", views.testimonials, name="testimonials"),
    path("case-studies/", views.case_studies, name="case_studies"),
    path("blog/", views.blog, name="blog"),
    path("pricing/", views.pricing, name="pricing"),
]