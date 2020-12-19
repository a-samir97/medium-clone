from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from accounts.models import User
from tag.models import Tag
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
    tags = models.ManyToManyField(Tag)
    clapped = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    objects = models.Manager() # Default Manager 
    posts = PostManager()
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        if self.status == 'P':
            self.publish = timezone.now()
            
        super(Post, self).save(*args, **kwargs)
