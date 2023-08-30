# Generated by Django 4.2.4 on 2023-08-28 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_remove_user_posts"),
        ("content", "0006_content_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="user.user",
            ),
        ),
    ]
