from django.urls import path
from comment.view import CommentView

urlpatterns = [
    path('/comments/', CommentView.as_view(), name='create_comment'),
    path('/comments/<int:comment_id>/', CommentView.as_view(), name='manage_comment'),
]
