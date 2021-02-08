from django.urls import path

from . import views

app_name = 'vote'

urlpatterns = [
    path('toggle-upvote/<int:post_id>/',
         views.ToggleUpvoteAPIView.as_view(), name='toggle-upvote'),
    path('toggle-downvote/<int:post_id>/',
         views.ToggleDownvoteAPIView.as_view(), name='toggle-downvote'),
    path('upvote-counts/<int:post_id>/',
         views.UpvotePostCountsAPIView.as_view(), name='upvote-count'),
    path('downvote-counts/<int:post_id>/',
         views.DownvotePostCountsAPIView.as_view(), name='downvote-counts')
]
