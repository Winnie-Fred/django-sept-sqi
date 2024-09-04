from django.urls import path
from contact import views

urlpatterns = [
    path('contact-us/', views.contact, name='contact'),
    path('email/', views.email, name="email"),
]