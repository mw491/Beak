# Generated by Django 4.1.3 on 2022-12-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chirps", "0005_alter_chirp_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chirp",
            name="content",
            field=models.TextField(max_length=280),
        ),
    ]