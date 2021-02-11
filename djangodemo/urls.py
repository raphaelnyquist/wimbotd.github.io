from django.urls import path
from . import views

app_name = "djangodemo"

urlpatterns = [
    path("", views.index, name="index")
]