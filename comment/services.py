from django.shortcuts import get_object_or_404
from .models import Comment, ArticleCommentCount
from comment.Repository import CommentRepository, ArticleCommentCountRepository
from .serializers import CommentResponse
from django.db import transaction


class CommentService:

    @staticmethod
    @transaction.atomic
    def create(data):
        parent = CommentService.find_parent(data)
        comment = Comment.objects.create(
            comment=data['content'],
            parent_comment_id=parent.comment_id if parent else None,
            article_id=data['article_id'],
            writer_id=data['writer_id']
        )
        ArticleCommentCountRepository.increase(data['article_id'])
        return CommentResponse(comment).data

    @staticmethod
    def read(comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        return CommentResponse(comment).data

    @staticmethod
    def read_all(article_id, page, page_size):
        offset = (page - 1) * page_size
        comments = CommentRepository.find_all(article_id, offset, page_size)
        total_count = CommentRepository.count_by(article_id, None, page_size)
        return {
            "comments": CommentResponse(comments, many=True).data,
            "comment_count": total_count
        }

    @staticmethod
    @transaction.atomic
    def delete(comment_id):
        comment = get_object_or_404(Comment, pk=comment_id)
        if not comment.deleted:
            if CommentService.has_children(comment):
                comment.delete_comment()
            else:
                comment.delete()
            ArticleCommentCountRepository.decrease(comment.article_id)

    @staticmethod
    def has_children(comment):
        return CommentRepository.count_by(comment.article_id, comment.comment_id, 2) > 1

    @staticmethod
    def find_parent(data):
        parent_id = data.get('parent_comment_id')
        if parent_id is None:
            return None
        return Comment.objects.filter(comment_id=parent_id, deleted=False).first()
