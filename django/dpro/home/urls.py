from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("detail/<int:id>", views.details, name="detail")
]