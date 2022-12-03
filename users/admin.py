from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ["user", "bio", "date_created"]
