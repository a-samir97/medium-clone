from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .serializers import ShowCollectionSerializer, CreateCollectionSerializer
from .models import Collection
from .permissions import IsOwner


class CollectionViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ShowCollectionSerializer
        else:
            return CreateCollectionSerializer

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (permissions.AllowAny,)
        elif self.action == 'create':
            permission_classes = (permissions.IsAuthenticated,)
        elif self.action == 'update' or self.action == 'partial_update' \
                or self.action == 'destroy':
            permission_classes = (permissions.IsAuthenticated, IsOwner)
        else:
            permission_classes = (permissions.IsAdminUser,)

        return [permission() for permission in permission_classes]

    def create(self, request):
        collection_serializer = CreateCollectionSerializer(data=request.data)
        if collection_serializer.is_valid():
            collection_serializer.save(user=request.user)
            return Response(
                collection_serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                collection_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
