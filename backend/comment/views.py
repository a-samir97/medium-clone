from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from .models import Comment
from posts.models import Post

from .serializers import CommentSerializer

class CommentViewSetAPI(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

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
            comment_serializer = CommentSerializer(data=request.data)
            if comment_serializer.is_valid():
                comment_serializer.save()
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
            comment_serializer = CommentSerializer(instance=comment, data=request.data)
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
            comment_serializer = CommentSerializer(instance=comment, data=request.data)
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
