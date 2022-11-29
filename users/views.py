from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegisterForm


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
            return redirect("ui-home")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})
