# Generated by Django 4.2.4 on 2023-08-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0003_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="posts",
            field=models.ManyToManyField(to="content.content"),
        ),
    ]
