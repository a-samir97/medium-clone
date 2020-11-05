from rest_framework import serializers
from .models import User, SocialAccounts


class SocialAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccounts
        fields = ('facebook', 'github', 'twitter', 'linkedin')
    

class SignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'image')


    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            image=validated_data['image'] or None
        )
        user.set_password(validated_data['password'])
        user.save()

        return user