from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

# Create your views here.

def index(request):
    pics=Photo.objects.all()
    return render(request, 'pictures/index.html',{"pics":pics})