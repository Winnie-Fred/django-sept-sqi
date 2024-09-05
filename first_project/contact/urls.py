from django.urls import path

from . import views

urlpatterns = [
    path('email/', views.email, name="email"),
    path('phone-us/', views.phone, name='phone'),
]