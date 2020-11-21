from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from .models import Post
from .serializers import PostSerializer

class UserPublishedPostsListAPI(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.posts.get_published_posts().filter(author=self.request.user)

class UserDraftedPostsListAPI(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(status="D")

class MostClappedPostListAPI(ListAPIView):
    queryset = Post.posts.get_most_clapped_posts()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

class LatestPostListAPI(ListAPIView):
    queryset = Post.posts.get_recent_posts()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.posts.get_published_posts()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (permissions.AllowAny,)

        elif self. action == 'create' or self.action == 'update' or \
                self.action == 'destroy' or self.action == 'partial_update':

            permission_classes = (permissions.IsAuthenticated,)
        
        else:
            permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        
        return [permission() for permission in permission_classes]

 