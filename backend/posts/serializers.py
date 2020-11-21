from rest_framework import serializers
from .models import Post

from accounts.serializers import ShowUserSerializer

class PostCreationSerializer(serializers.ModelSerializer):
    #author = ShowUserSerializer()
    class Meta:
        model = Post
        exclude = ('slug', 'views', 'clapped')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"