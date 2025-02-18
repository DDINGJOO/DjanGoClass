from rest_framework import serializers
from .models import Comment, ArticleCommentCount


class CommentCreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['article_id', 'content', 'parent_comment_id', 'writer_id']


class CommentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment_id', 'content', 'parent_comment_id', 'article_id', 'writer_id', 'deleted', 'created_at']


class CommentPageResponseSerializer(serializers.Serializer):
    comments = CommentResponseSerializer(many=True)
    comment_count = serializers.IntegerField()
