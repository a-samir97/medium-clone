from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet,
    MostClappedPostListAPI,
    LatestPostListAPI,
    UserPublishedPostsListAPI,
    UserDraftedPostsListAPI,
    ClappPostsAPI
)

app_name = 'posts'

router = DefaultRouter()

router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('most-clapped/', MostClappedPostListAPI.as_view(), name='most-clapped'),
    path('latest/', LatestPostListAPI.as_view(), name='latest-posts'),
    path('published/', UserPublishedPostsListAPI.as_view(), name='published-posts'),
    path('drafted/', UserDraftedPostsListAPI.as_view(), name='drafted-posts'),
    path('clapp/<int:id>/', ClappPostsAPI.as_view(), name='clapp-post'),

] + router.urls


