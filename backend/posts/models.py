from django.db import models
from django.utils import timezone
from accounts.models import User
from .managers import PostManager

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
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
    tags = models.ManyToManyField(Tag)
    clapped = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
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

class Upvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')

    def __str__(self):
        return self.user.username + " likes " + self.post.title

class Downvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_unlikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_unlikes')


    def __str__(self):
        return self.user.username + " unlikes " + self.post.title

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collections')
    name = models.CharField(max_length=30)
    posts = models.ManyToManyField(Post)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name