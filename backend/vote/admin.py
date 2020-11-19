from django.contrib import admin

from .models import Upvote, Downvote

admin.site.register(Upvote)
admin.site.register(Downvote)