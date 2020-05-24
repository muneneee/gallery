from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Photo, Location

# Create your views here.

def index(request):
    pics=Photo.objects.all()
    return render(request, 'pictures/index.html',{"pics":pics})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, "pictures/search.html",{"message":message, "categories":searched_categories})
    

    else:
        message = "You haven't searched for any term"
        return render(request, 'pictures/search.html', {"message":message})


def filter_location(request, location):
    locations = Location.objects.all()
    locatio = Location.get_location_id(location)
    images = Photo.filter_by_location(location)
    title= f'{location} photos'

    return render(request,'location.html',{"title":title, "images":images, "locations":locations, "locatio":locatio})



def photo(request,photo_id):
    try:
        photo = Photo.objects.get(id = photo_id)

    except DoesNotExist:
        raise Http404()
    return render(request, "pictures/photo.html", {"photo":photo})
