from django.shortcuts import render, redirect
from django.db.models import prefetch_related_objects

from .models import User

def index(request):
    all_users = User.objects.all()

    [u.load_posts() for u in all_users]

    return render(request, "user/index.html", context={
        'users': all_users
    })

def new_user(request):
    return render(request, "user/new.html")

def create(request):
    new_user = User(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
    )
    new_user.save()

    return redirect("/user")
