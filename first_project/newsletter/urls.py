from django.urls import path
from . import views

urlpatterns = [
    path("subscribe-to-newsletter/", views.subscribe, name="subscribe")
]