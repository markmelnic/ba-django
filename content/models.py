from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=400)
    # create relationship with User
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='posts'
    )
