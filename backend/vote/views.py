from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Downvote, Upvote
from posts.models import Post


class ToggleUpvoteAPIView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        if post:
            upvote = Upvote.objects.filter(user=request.user, post=post)

            if upvote:
                upvote.delete()
                return Response(
                    {"data": "upvote removed"},
                    status=status.HTTP_200_OK
                )
            else:
                Upvote.objects.create(user=request.user, post=post)
                return Response(
                    {"data": "upvote added"},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"error": "post is not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class ToggleDownvoteAPIView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        if post:
            downvote = Downvote.objects.filter(user=request.user, post=post)

            if downvote:
                downvote.delete()
                return Response(
                    {"data": "downvote removed"},
                    status=status.HTTP_200_OK
                )
            else:
                Downvote.objects.create(user=request.user, post=post)
                return Response(
                    {"data": "downvote added"},
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"error": "post is not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class UpvotePostCountsAPIView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()
        if post:
            upvote_count = Upvote.objects.filter(post=post).count()
            return Response(
                {"data": upvote_count},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "post is not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class DownvotePostCountsAPIView(APIView):

    permission_classes = (permissions.AllowAny,)

    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id).first()

        if post:
            downvote_count = Downvote.objects.filter(post=post).count()
            return Response(
                {"data": downvote_count},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "post is not found"},
                status=status.HTTP_404_NOT_FOUND
            )
