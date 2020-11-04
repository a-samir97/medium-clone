from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    image = models.ImageField()
    following = models.ManyToManyField (
        'self', 
        through='UserFollowing', 
        related_name='followers', 
        symmetrical=False
    )
    def __str__(self):
        return self.username

class UserFollowing(models.Model):
    user_following = models.ForeignKey(User, related_name='rel_followed', on_delete=models.CASCADE)
    user_followed = models.ForeignKey(User,related_name='rel_following' ,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_follow.username + " follow " + self.user_followed.username