from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Post
from .serializers import (
    PostSerializer,
    PostCreationSerializer
)
from .permissions import IsOwner


class UserPublishedPostsListAPI(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.posts.get_published_posts().filter(
            author=self.request.user
        )


class UserDraftedPostsListAPI(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(status="D", author=self.request.user)


class MostClappedPostListAPI(ListAPIView):
    queryset = Post.posts.get_most_clapped_posts()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)


class LatestPostListAPI(ListAPIView):
    queryset = Post.posts.get_recent_posts()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)


class ClappPostAPI(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, id):
        post = get_object_or_404(Post, id=id)
        post.clapped += 1
        post.save()
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.posts.get_published_posts()
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PostSerializer
        else:
            return PostCreationSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (permissions.AllowAny,)

        elif self. action == 'create':
            permission_classes = (permissions.IsAuthenticated,)

        elif self.action == 'update' or self.action == 'destroy' or \
                self.action == 'partial_update':
            permission_classes = (permissions.IsAuthenticated, IsOwner)

        else:
            permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

        return [permission() for permission in permission_classes]

    def create(self, request):
        serializer = PostCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        post.views += 1
        post.save()
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)
