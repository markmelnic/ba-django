from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User

@login_required # middleware
def index(request):
    current_user = request.user
    current_user.load_posts()

    return render(request, "user/index.html", context={
        'user': current_user
    })

def login_user(request):
    if request.method == "GET":
        return render(request, "user/login.html")
    elif request.method == "POST":
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user:
            login(request, user)
            return redirect("/user")
        else:
            return redirect("/user/login")

def register(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        new_user = User.objects.create_user(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            username = request.POST['username'],
            password = request.POST['password'],
        )
        new_user.save()

        return redirect("/user")

def logout_user(request):
    logout(request)
    return redirect('/')
