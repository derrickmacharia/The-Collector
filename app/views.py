from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from app.models import photos

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


