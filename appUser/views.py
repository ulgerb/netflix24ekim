from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # kullanıcı fonksiyonları
from django.contrib.auth.models import User
from appUser.models import *

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
            if not User.objects.filter(username = username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(first_name=name, last_name=surname, email=email, username=username, password=password1)
                    user.save()
                    return redirect("loginUser")
                else:
                    return render(request, 'users/register.html', {"hata": "Bu mail üzerine daha önceden hesap oluşturulmuş!"})
            else:
                return render(request, 'users/register.html', {"hata": "Bu kulanıcı adı daha önceden alınmış!"})
        else:
            return render(request, 'users/register.html', {"hata": "şifreler aynı değil!"})
            
            
    return render(request,'users/register.html')

# Çıkış yap
def logoutUser(request):
    logout(request)
    return redirect('index')

def Account(request, id):
    profil = Profil.objects.get(id=id)
    account = '/account/'+ id + '/'
    context = {
        'profil': profil,
        'account': account,
    }
    return render(request,'users/hesap.html', context)

# Şifre değiştir
def changePassword(request):
    
    if request.method == "POST":
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1==password2:
            user = User.objects.get(username = request.user)
            user.set_password(password1)
            user.save()
            return redirect('loginUser')
    
    return render(request,'users/changepassword.html')


