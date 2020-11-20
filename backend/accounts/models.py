from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    image = models.ImageField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    following = models.ManyToManyField (
        'self', 
        through='UserFollowing', 
        related_name='followers', 
        symmetrical=False
    )
    def __str__(self):
        return self.username

class SocialAccounts(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_accounts', null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# Intermediate Model for many to mant relation
class UserFollowing(models.Model):
    user_following = models.ForeignKey(User, related_name='rel_followed', on_delete=models.CASCADE)
    user_followed = models.ForeignKey(User,related_name='rel_following' ,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_follow.username + " follow " + self.user_followed.username


class ResetPasswordToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField()

    def __str__(self):
        return self.user.username


class ConfirmationEmailToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField()

    def __str__(self):
        return self.user.username