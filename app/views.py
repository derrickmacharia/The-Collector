from django.http.response import Http404
from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from app.models import Category, Location, photos
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    categories = Category.objects.all()
    locations = Location.objects.all()
    
        
    if 'location' in request.GET and request.GET["location"]:
        location_id = request.GET.get("location")
        photoapp = photos.objects.filter(location = location_id)
       
    else:
        photoapp = photos.objects.all()
            
    ctx = {'photoapp':photoapp, 'categories': categories, 'locations':locations }
    return render(request, 'all-photos/index.html',ctx)

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

