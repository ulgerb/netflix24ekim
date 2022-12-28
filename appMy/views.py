from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def browseIndex(request):
    return render(request,'browse-index.html')

def Browse(request):
    return render(request,'browse.html')

