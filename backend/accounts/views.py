from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.generics import GenericAPIView

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
