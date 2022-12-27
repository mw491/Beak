from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField


class Chirp(models.Model):
    id = ShortUUIDField(primary_key=True)
    content = models.TextField(max_length=280)
    date_chirped = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    up_votes = models.ManyToManyField(User, related_name="chirp_up_votes")
    down_votes = models.ManyToManyField(User, related_name="chirp_down_votes")

    def up_votes_count(self):
        return self.up_votes.count()

    def down_votes_count(self):
        return self.down_votes.count()