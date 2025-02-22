from rest_framework import serializers
from .models import Comment, ArticleCommentCount


class CommentCreateRequest(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article_id', 'content', 'parent_comment_id', 'writer_id']


class CommentResponse(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'content', 'parent_comment_id', 'article_id', 'writer_id', 'deleted', 'created_at']


class CommentPageResponse(serializers.Serializer):
    comments = CommentResponse(many=True)
    comment_count = serializers.IntegerField()
