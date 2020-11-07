from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token

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
