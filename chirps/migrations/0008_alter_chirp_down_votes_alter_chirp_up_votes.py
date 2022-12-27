# Generated by Django 4.1.3 on 2022-12-27 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chirps", "0007_chirp_down_votes_chirp_up_votes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chirp",
            name="down_votes",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="down_votes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="chirp",
            name="up_votes",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="up_votes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
