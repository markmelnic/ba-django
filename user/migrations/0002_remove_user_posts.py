# Generated by Django 4.2.4 on 2023-08-23 19:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="posts",
        ),
    ]
