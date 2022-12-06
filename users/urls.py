from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.signin, name="login"),
    path("logout/", views.signout, name="logout"),
    path("<str:username>/profile/", views.profile, name="profile"),
    path("<str:username>/profile/edit",
         views.change_profile, name="profile-edit"),
]
