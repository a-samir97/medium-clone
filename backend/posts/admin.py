from django.contrib import admin
from .models import Post, Comment, Upvote, Downvote, Collection

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(Downvote)
admin.site.register(Collection)