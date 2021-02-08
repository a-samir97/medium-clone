from django.contrib import admin
from .models import (
    User,
    UserFollowing,
    SocialAccounts,
    ResetPasswordToken,
    ConfirmationEmailToken
)

admin.site.register(User)
admin.site.register(UserFollowing)
admin.site.register(SocialAccounts)
admin.site.register(ResetPasswordToken)
admin.site.register(ConfirmationEmailToken)
