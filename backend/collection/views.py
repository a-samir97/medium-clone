from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .serializers import ShowCollectionSerializer, CreateCollectionSerializer
from .models import Collection

class CollectionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCollectionSerializer
        else:
            return ShowCollectionSerializer

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (permissions.AllowAny,)
        elif self.action == 'create':
            permission_classes = (permissions.IsAuthenticated,)
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = (permissions.IsAuthenticated,)
        else:
            permission_classes = (permissions.IsAdminUser,)
        
        return [permission() for permission in permission_classes]
    
    
