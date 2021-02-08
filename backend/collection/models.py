from django.db import models
from accounts.models import User
from posts.models import Post


class Collection(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
