# Generated by Django 3.1.3 on 2020-11-24 21:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_email_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', through='accounts.UserFollowing', to=settings.AUTH_USER_MODEL),
        ),
    ]
