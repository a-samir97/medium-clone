from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (permissions.AllowAny,)

        elif self. action == 'create' or self.action == 'update' or \
                self.action == 'destroy' or self.action == 'partial_update':

            permission_classes = (permissions.IsAuthenticated,)
        
        else:
            permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        

        return [permission() for permission in permission_classes]

            