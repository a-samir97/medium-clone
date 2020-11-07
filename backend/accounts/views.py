from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication

from .models import User, SocialAccounts
from .serializers import SignupSerializer

class SignupAPIView(GenericAPIView):
    """
        Signup class API view to create a new user 
        params:
            - username (required)
            - email (required)
            - password (required)
            - image (optional)
            - social accounts (optional), require URL 
    """
    serializer_class = SignupSerializer

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

class SocialAccountsAPIView(APIView):
    '''
        SocialAccounts API class for adding social accounts for existing user

        params:
            - Facebook
            - GitHub
            - Twitter
            - Linkedin
    '''
    authentication_classes = (TokenAuthentication,)

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