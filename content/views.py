from django.shortcuts import render, redirect

from .models import Content
from user.models import User

def index(request):
    all_posts = Content.objects.all()
    return render(request, "content/index.html", context={
        'posts': all_posts
    })

def new_page(request):
    users = User.objects.all()
    return render(request, "content/new.html", context={
        "users": users
    })

def edit_page(request, post_id):
    post = Content.objects.get(id=post_id)
    return render(request, "content/edit.html", context={
        "post": post
    })

def create(request):
    new_post = Content(
        **request.POST
        # title = request.POST['title'],
        # text = request.POST['text'],
        # user_id = request.POST['user_id'],
    )
    new_post.save()

    return redirect("/")

def update(request, post_id):
    post = Content.objects.get(id=post_id)
    post.title = request.POST['title']
    post.text = request.POST['text']
    post.save()

    return redirect("/")

def delete(request, post_id):
    post = Content.objects.get(id=post_id)
    post.delete()

    return redirect("/")
