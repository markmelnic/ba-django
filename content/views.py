from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Content

def index(request):
    all_posts = Content.objects.all()
    return render(request, "content/index.html", context={
        'posts': all_posts
    })

@login_required
def new_page(request):
    return render(request, "content/new.html")

@login_required
def edit_page(request, post_id):
    post = Content.objects.get(id=post_id)
    return render(request, "content/edit.html", context={
        "post": post
    })

@login_required
def create(request):
    new_post = Content(
        title = request.POST['title'],
        text = request.POST['text'],
        user_id = request.user.id,
    )
    new_post.save()

    return redirect("/")

@login_required
def update(request, post_id):
    post = Content.objects.get(id=post_id)
    post.title = request.POST['title']
    post.text = request.POST['text']
    post.save()

    return redirect("/")

@login_required
def delete(request, post_id):
    current_user = request.user
    current_user.load_posts()

    user_post_ids = [p.id for p in current_user.post_list]

    if int(post_id) in user_post_ids:
        post = Content.objects.get(id=post_id)
        post.delete()

    return redirect("/")
