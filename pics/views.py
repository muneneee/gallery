from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

# Create your views here.

def index(request):
    pics=Photo.objects.all()
    return render(request, 'pictures/index.html',{"pics":pics})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories =Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, "pictures/search.html",{"message":message, "categories":searched_categories})
    

    else:
        message = "You haven't searched for any term"
        return render(request, 'pictures/search.html', {"message":message})