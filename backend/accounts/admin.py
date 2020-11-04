from django.contrib import admin
from .models import User, UserFollowing, SocialAccounts

admin.site.register(User)
admin.site.register(UserFollowing)
admin.site.register(SocialAccounts)