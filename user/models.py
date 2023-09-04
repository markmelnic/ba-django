from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(default="")

    def load_posts(self):
        self.post_list = self.posts.all()

    def __str__(self):
        return f"<User {self.first_name} {self.last_name}>"
