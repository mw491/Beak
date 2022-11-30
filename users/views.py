from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

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
                f"A new bird has hatched! Welcome to the new world, {name}!",
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
            return redirect("ui-home")
        else:
            messages.error(request, "Username or Password incorrect. Please try again.")

    return render(request, "users/login.html", {"form": LoginForm()})


# def login(request):
#     form = LoginForm(request.POST or None)
#     if request.POST and form.is_valid():
#         user = form.login(request)
#         if user:
#             login(request, user)
#             return redirect("ui-home")  # Redirect to a success page.
#     return render(request, "users/login.html", {"form": form})
