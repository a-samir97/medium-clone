from rest_framework import serializers
from .models import Collection


class CreateCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        exclude = ('created_at', 'updated_at', 'user')


class ShowCollectionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Collection
        fields = "__all__"
