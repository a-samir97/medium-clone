from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Tag
from .serializers import TagSerializer

class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)