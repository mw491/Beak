# Generated by Django 4.1.3 on 2022-12-27 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chirps", "0010_chirp_down_votes_chirp_up_votes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chirp",
            name="down_votes",
        ),
        migrations.RemoveField(
            model_name="chirp",
            name="up_votes",
        ),
        migrations.AddField(
            model_name="chirp",
            name="down_votes",
            field=models.ManyToManyField(
                related_name="chirp_down_votes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chirp",
            name="up_votes",
            field=models.ManyToManyField(
                related_name="chirp_up_votes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
