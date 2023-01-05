from django.shortcuts import render, redirect
from appUser.models import *
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')

def Browse(request):
    profils = Profil.objects.filter(user=request.user.id)
    # girişli olan kullanıcını profillerini say, 4se eklemesin, 
    context = {"profils": profils,}
    if len(profils) < 4:
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            
            profil = Profil(name = name, image=image,user=request.user )
            profil.save()
            return redirect('Browse')
    else:
        context.update({'hata':'Maximum profil sayısına ulaştınız'})
    
    return render(request,'browse.html',context)

def profilDel(request,id):
    profil = Profil.objects.get(id=id)
    profil.delete()
    return redirect('Browse')

def BrowseIndex(request, id):
    profil = Profil.objects.get(id=id)
    videos = Video.objects.all()
    
    context = {
        "profil":profil,
        "videos":videos,
    }
    
    return render(request,'browse-index.html',context)
