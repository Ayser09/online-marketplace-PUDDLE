from django.urls import path
from . import views

app_name = "dasbhboard"

urlpatterns = [
    path("", views.index, name="index"),
]
