from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # kullanıcı fonksiyonları
from django.contrib.auth.models import User

# Create your views here.

# Giriş yap
def loginUser(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Browse')
        else:
            return render(request, 'users/login.html', {'hata':'Kullanıcı adı veya şifre yanlış!'})
            
    return render(request,'users/login.html')

# Kaydol

def registerUser(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 == password2:
            user = User.objects.create_user(first_name=name, last_name=surname, email=email, username=username, password=password1)
            user.save()
            
            
    return render(request,'users/register.html')

# Şifre değiştir



