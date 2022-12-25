from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField


class Chirp(models.Model):
    id = ShortUUIDField(primary_key=True)
    content = models.TextField(max_length=280)
    date_chirped = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
