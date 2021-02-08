from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreattionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('author', 'post')
