from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from posts.models import Post

from .serializers import CommentSerializer, CommentCreattionSerializer
from .models import Comment
from .permissions import IsOwner

class CommentViewSetAPI(viewsets.ModelViewSet):

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = (permissions.AllowAny,)
        
        elif self.action == 'create':
            permission_classes = (permissions.IsAuthenticated,)
        
        else:
            permission_classes = (permissions.IsAuthenticated, IsOwner)
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CommentSerializer
        else:
            return CommentCreattionSerializer

    def list(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()

        if post:
            queryset = Comment.objects.filter(post=post)
            comments_serializer = CommentSerializer(queryset, many=True)
        
            return Response(
                {"data": comments_serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "post is not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def retrieve(self, request, comment_id):

        permission_classes = (permissions.AllowAny,)

        comment = Comment.objects.filter(id=comment_id).first()
        if comment:
            comment_serializer = CommentSerializer(comment)
            return Response(
                {"data": comment_serializer.data},
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                    {"error": 'comment is not found'},
                    status=status.HTTP_404_NOT_FOUND
                )

    def create(self, request, post_id):
        permission_classes = (permissions.IsAuthenticated,)

        post = Post.objects.filter(id=post_id).first()
        if post:
            comment_serializer = CommentCreattionSerializer(data=request.data)
            if comment_serializer.is_valid():
                comment_serializer.save(post=post, author=request.user)
                return Response(
                    {"data": comment_serializer.data},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"error": comment_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"error": "post is not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def partial_update(self, request, comment_id):
        comment = Comment.objects.filter(id=comment_id).first()
        if comment:
            comment_serializer = CommentCreattionSerializer(instance=comment, data=request.data)
            if comment_serializer.is_valid():
                return Response(
                    {"data": comment_serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"data": comment_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    {"data": "comment is not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

    def update(self, request, comment_id):
        comment = Comment.objects.filter(id=comment_id).first()
        if comment:
            comment_serializer = CommentCreattionSerializer(instance=comment, data=request.data)
            if comment_serializer.is_valid():
                comment_serializer.save()
                return Response(
                    {"data": comment_serializer.data},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"data": comment_serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    {"data": "comment is not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

    def destroy(self, request, commment_id):
        comment = Comment.objects.filter(id=comment_id).first()
        if comment:
            comment.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                {"error": "comment is not found"},
                status=status.HTTP_404_NOT_FOUND
            )
