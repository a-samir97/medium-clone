from rest_framework import serializers
from .models import Post

from accounts.serializers import ShowUserSerializer

class PostCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = (
            'slug', 'views', 
            'clapped', 'author',
            'publish'
            )

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = "__all__"