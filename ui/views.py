from django.shortcuts import render
from chirps.models import Chirp


def home(request):
    context = {"chirps": Chirp.objects.order_by('date_chirped').reverse()}
    return render(request, "ui/home.html", context)
