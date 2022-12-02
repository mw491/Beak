from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from chirps.models import Chirp
from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = (
                form.cleaned_data.get("first_name")
                + " "
                + form.cleaned_data.get("last_name")
            )
            messages.success(
                request,
                f"A new bird has hatched successfully! Welcome to the new world, {name}! You are now able to login.",
            )
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("ui-home")
        else:
            messages.error(
                request, "Username or Password incorrect. Please try again.")

    return render(request, "users/login.html", {"form": LoginForm()})


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("ui-home")


def profile(request, username):
    profile_user = User.objects.get(username=username)
    profile_chirps = Chirp.objects.all().filter(author=profile_user)
    return render(request, "users/profile.html", context={"profile_user": profile_user, "profile_chirps": profile_chirps})
