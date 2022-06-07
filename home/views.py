from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
# password for test user: pepperp00ts

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/register")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        #check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            #A backend authenticated the credentials
            return redirect("/")
        else:
            #No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/index.html")       