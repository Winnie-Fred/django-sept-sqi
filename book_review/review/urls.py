from django.urls import path

from . import views

app_name = "review"

urlpatterns = [
    path("create-review/<int:book_id>", views.create_review, name="create_review")
]