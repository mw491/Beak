from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from chirps.models import Chirp
from users.models import Profile
from .forms import RegisterForm, LoginForm, ChangeUserForm, ChangeProfileForm, CreateChirpForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = (
                form.cleaned_data.get("first_name")
                + " "
                + form.cleaned_data.get("last_name")
            )
            messages.success(
                request,
                f"A new bird has hatched successfully! Welcome to the new world, {name}! You are now able to login.",
            )
            Profile.objects.create(user=user)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form, "title": "Sign up for Beak"})


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

    return render(request, "users/login.html", {"form": LoginForm(), "title": "Login to Beak"})


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("ui-home")


def profile(request, username):
    profile_user = User.objects.get(username=username)
    profile_chirps = Chirp.objects.all().filter(
        author=profile_user).order_by('date_chirped').reverse()
    profile_profile = profile_user.profile
    return render(request, "users/profile.html", context={"profile_user": profile_user, "profile_chirps": profile_chirps, "profile": profile_profile, "title": f"{profile_user.get_full_name()}'s Profile"})


@ login_required
def change_profile(request, username):
    user = request.user
    edit_user = User.objects.get(username=username)
    if user == edit_user:
        if request.method == "POST":
            user_form = ChangeUserForm(request.POST, instance=user)
            profile_form = ChangeProfileForm(
                request.POST, instance=user.profile)
            if user_form.is_valid and profile_form.is_valid:
                user_form.save()
                profile_form.save()
                messages.success(
                    request, "Account information changed successfully")
                return redirect("ui-home")
        else:
            user_form = ChangeUserForm(instance=user)
            profile_form = ChangeProfileForm(instance=user.profile)
        return render(request, "users/change_profile.html", {"user_form": user_form, "profile_form": profile_form, "username": user.username, "title": "Edit your Profile"})
    raise PermissionDenied()
