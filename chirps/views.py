from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Chirp


def view_post(request, username, id):
    if request.POST:
        Chirp.objects.filter(id=id).delete()
        messages.success("Post successfully deleted")
        return redirect("ui-home")
    author = User.objects.get(username=username)
    chirp = Chirp.objects.get(id=id, author=author)

    return render(request, "chirps/view_chirp.html", {"chirp": chirp, "user": request.user})
