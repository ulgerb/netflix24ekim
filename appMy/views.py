from django.shortcuts import render
from appUser.models import *
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')

def Browse(request):
    profils = Profil.objects.filter(user=request.user.id)
    
    context = {
        "profils":profils,
    }
    return render(request,'browse.html',context)

def BrowseIndex(request, id):
    profil = Profil.objects.get(id=id)
    videos = Video.objects.all()
    
    context = {
        "profil":profil,
        "videos":videos,
    }
    
    return render(request,'browse-index.html',context)
