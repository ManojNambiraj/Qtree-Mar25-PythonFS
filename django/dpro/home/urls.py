from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<str:slug>", views.details, name="detail")
]