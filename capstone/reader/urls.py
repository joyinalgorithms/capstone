from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("discover", views.discover, name="discover"),
    path("my-library", views.mylibrary, name="my-library"),
    path("reading-lists", views.readinglists, name="reading-lists"),
    path("saved-quote", views.savedquote, name="saved-quote"),
    path("profile", views.profile, name="profile"),

]