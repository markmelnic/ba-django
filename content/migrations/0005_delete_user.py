# Generated by Django 4.2.4 on 2023-08-23 16:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0004_user_posts"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]