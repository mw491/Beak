from django.shortcuts import render
from chirps.models import Chirp


def home(request):
    context = {"chirps": Chirp.objects.all()}
    return render(request, "ui/home.html", context)
