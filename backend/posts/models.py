from django.db import models
from django.utils import timezone
from accounts.models import User
from .managers import PostManager

class Post(models.Model):
    """
        Model for Post Table
    """

    STATUS_CHOICES = (
        ("D", "Draft"),
        ("P", "Published")
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    clapped = models.IntegerField(default=0)

    posts = PostManager()
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    """
        Model for Comment Table
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.body