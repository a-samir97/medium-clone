from django.db import models
from posts.models import Post
from accounts.models import User


class Upvote(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_likes')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_likes')

    def __str__(self):
        return self.user.username + " likes " + self.post.title


class Downvote(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_unlikes')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_unlikes')

    def __str__(self):
        return self.user.username + " unlikes " + self.post.title
