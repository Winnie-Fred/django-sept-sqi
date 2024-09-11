from django.urls import path

from . import views

urlpatterns = [
    path("demo-view-1/", views.demo_view_one, name="demo_view_one"),
    path("demo-view-2/", views.demo_view_two, name="demo_view_two"),
]