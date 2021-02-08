from django.urls import path
from .views import CommentViewSetAPI

app_name = 'comment'


get_all_post_commens = CommentViewSetAPI.as_view({"get": "list"})

create_comment = CommentViewSetAPI.as_view({"post": "create"})

comment_details = CommentViewSetAPI.as_view({
    "get": "retrieve",
    "delete": "destroy",
    "put": "update",
    "patch": "partial_update"
})


urlpatterns = [

    path('all/<int:post_id>/', get_all_post_commens, name='post-comments'),
    path('create/<int:post_id>/', create_comment, name='create-comment'),
    path('<int:comment_id>/', comment_details, name='comment-details'),
]
