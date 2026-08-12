from django.shortcuts import render
from django.urls import path
from . import views
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Nossa primeira aplicação Django.</h1>")

urlpatterns = [
    path("", views.index),
]

# Create your views here.
