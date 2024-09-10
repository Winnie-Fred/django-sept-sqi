from django.urls import path

from . import views

urlpatterns = [
    path("dtl/", views.new_view, name="dtl"),
]