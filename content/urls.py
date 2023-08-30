from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new_page, name="new_post"),
    path("edit/<post_id>", views.edit_page, name="edit_post"),
    path("create", views.create, name="create_post"),
    path("update/<post_id>", views.update, name="update_post"),
    path("delete/<post_id>", views.delete, name="delete_post"),
]
