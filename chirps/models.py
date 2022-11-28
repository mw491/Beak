from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField


class Chirp(models.Model):
    id = ShortUUIDField(prefix="id_", primary_key=True)
    content = models.TextField()
    date_chirped = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
