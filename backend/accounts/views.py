import uuid
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .models import (
    User, 
    SocialAccounts, 
    ResetPasswordToken, 
    ConfirmationEmailToken
)
from .serializers import SignupSerializer

class SignupAPIView(GenericAPIView):
    """
        Signup class API view to create a new user 
        params:
            - username (required)
            - email (required)
            - password (required)
            - image (optional)
    """
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data

        # check if username and password exist in requested data
        if not data.get('username') or not data.get('password'):
            return Response({"error": "please make sure to input data."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    '''
        Login API class to login user to our website
        
        params:
            - username
            - password
    '''
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data

        if not data.get('username') or not data.get('password'):
            return Response(
                {"error": "don't leave any input blank please"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=data['username'], password=data['password'])

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'invalid credentials.'},
                status=status.HTTP_404_NOT_FOUND
            )

class LogoutAPIView(APIView):

    def post(self, request):

        if request.auth and request.user:
            Token.objects.get(user=request.user).delete()
            return Response(status=status.HTTP_200_OK)

class EmailConfirmation(APIView):
    def post(self, request):
        pass

class ResetPassword(APIView):

    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        
        # if the user doesn't put email 
        if not request.data.get('email'):
            return Response({"error": "please enter your email"}, status=status.HTTP_400_BAD_REQUEST)

        # if email doesn't exist in the database
        if not User.objects.filter(email=request.data.get('email')).exists():
            return Response({"error": "this email is not exist"}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(email=request.data.get('email'))
        
        reset_token = ResetPasswordToken.objects.create(user=user)
        reset_token.token = uuid.uuid4()

        # send email to user
        return Response({'token':reset_token.token}, status=status.HTTP_200_OK)


class ConfirmPassword(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, user_uuid):
        
        # check if uuid not exist in reset password tokens 
        if not ResetPasswordToken.objects.filter(token=user_uuid):
            return Response({"error": "invalid user"}, status=status.HTTP_400_BAD_REQUEST)
        
        # if user doesn't put password 
        if not request.data.get('password'):
            return Response({"error": "please enter new password"}, status=status.HTTP_400_BAD_REQUEST)

        password = request.data.get('password')

        user = ResetPasswordToken.objects.get(token=user_uuid).user
        user.set_password(password)
        user.save()
        ResetPasswordToken.objects.get(token=user_uuid).delete()
        return Response({"data": "Password Changed Successfully."}, status=status.HTTP_201_CREATED)

class SocialAccountsAPIView(APIView):
    '''
        SocialAccounts API class for adding social accounts for existing user

        params:
            - Facebook
            - GitHub
            - Twitter
            - Linkedin
    '''

    def post(self, request):

        if request.auth and request.user:
            
            data = request.data

            if not data.get('facebook') and not data.get('github') \
                and not data.get('twitter') and not data.get('linkedin'):

                return Response(
                    {"error": "at least you need to add one of them"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            user_accounts = SocialAccounts(
                facebook=data.get('facebook'),
                github=data.get('github'),
                twitter=data.get('twitter'),
                linkedin=data.get('linkedin'),
                user=request.user
            )  
            user_accounts.save()

            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "you are not authenticated user"},
                status=status.HTTP_401_UNAUTHORIZED
            )