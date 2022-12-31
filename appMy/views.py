from django.shortcuts import render
from appUser.models import Profil
# Create your views here.


def index(request):
    return render(request,'index.html')

def browseIndex(request):
    return render(request,'browse-index.html')

def Browse(request):
    profils = Profil.objects.filter(user=request.user.id)
    
    context = {
        "profils":profils,
    }
    return render(request,'browse.html',context)

def BrowseIndex(request, id):
    profil = Profil.objects.get(id=id)
    
    context = {
        "profil":profil,
    }
    
    return render(request,'browse-index.html',context)
