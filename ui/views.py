from django.shortcuts import render, redirect
from django.contrib import messages
from chirps.models import Chirp
from chirps.forms import CreateChirpForm


def home(request):
    user = request.user
    if request.method == "POST":
        form = CreateChirpForm(request.POST)
        if form.is_valid:
            content = request.POST.get("content")
            chirp = Chirp(content=content, author=user)
            chirp.save()
            messages.success(
                request, "Chirped Successfully")
            return redirect("ui-home")
    else:
        form = CreateChirpForm()
    context = {"chirps": Chirp.objects.order_by(
        'date_chirped').reverse(), "form": form}
    return render(request, "ui/home.html", context)
