from rest_framework import serializers
from .models import User, SocialAccounts


class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class SocialAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccounts
        fields = ('facebook', 'github', 'twitter', 'linkedin')


class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'}, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'image')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            image=validated_data.get('image')
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
