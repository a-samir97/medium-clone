from django.db import models
from django.contrib.auth.models import AbstractUser

class SocialAccounts(models.Model):
    facebook = models.URLField()
    github = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.facebook

class User(AbstractUser):
    
    accounts = models.ForeignKey(SocialAccounts, on_delete=models.DO_NOTHING, null=True, blank=True)
    image = models.ImageField()
    following = models.ManyToManyField (
        'self', 
        through='UserFollowing', 
        related_name='followers', 
        symmetrical=False
    )
    def __str__(self):
        return self.username

# Intermediate Model for many to mant relation
class UserFollowing(models.Model):
    user_following = models.ForeignKey(User, related_name='rel_followed', on_delete=models.CASCADE)
    user_followed = models.ForeignKey(User,related_name='rel_following' ,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_follow.username + " follow " + self.user_followed.username