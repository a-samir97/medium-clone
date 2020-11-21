from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    MostClappedPostListAPI,
    LatestPostListAPI,
    UserPublishedPostsListAPI,
    UserDraftedPostsListAPI
)

app_name = 'posts'

router = DefaultRouter()

router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('most-clapped/', MostClappedPostListAPI.as_view(), name='most-clapped'),
    path('latest-posts/', LatestPostListAPI.as_view(), name='latest-posts'),
    path('published-posts/', UserPublishedPostsListAPI.as_view(), name='published-posts'),
    path('drafted-posts/', UserDraftedPostsListAPI.as_view(), name='drafted-posts'),
    
] + router.urls


