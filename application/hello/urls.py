from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("siva", views.siva, name="siva"),
    path("karthi", views.karthi, name="karthi"),
    path("<str:name>", views.greet, name="greet")
]