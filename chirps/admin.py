from django.contrib import admin
from .models import Chirp


@admin.register(Chirp)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ["author", "content", "date_chirped"]
