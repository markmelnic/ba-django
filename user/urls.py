from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="user_index"),
    path("new", views.new_user, name="new_user"),
    path("create", views.create, name="create_user"),
]
