from django.urls import path 
from .views import TagListAPIView

app_name = 'tag'

urlpatterns = [
    path('', TagListAPIView.as_view(), name='tag-list'),
]
