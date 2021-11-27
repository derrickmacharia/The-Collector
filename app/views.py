from django.http.response import Http404
from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from app.models import photos
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


# def index(request):
#     return render(request, 'index.html')

def index(request):
    # imports photos and save it in database
    photoapp = photos.objects.all()
    # adding context 
    ctx = {'photoapp':photoapp}
    return render(request, 'all-photos/index.html', ctx)

def search_results(request):

    if 'photos' in request.GET and request.GET["photos"]:
        search_term = request.GET.get("photos")
        searched_photos = photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = photos.objects.get(id = photo_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-photos/photo.html", {"photo":photo})
