from django.db.models import Count
from .models import Comment, ArticleCommentCount


class CommentRepository:

    @staticmethod
    def count_by(article_id, parent_comment_id, limit):
        return Comment.objects.filter(article_id=article_id, parent_comment_id=parent_comment_id).count()

    @staticmethod
    def find_all(article_id, offset, limit):
        return Comment.objects.filter(article_id=article_id).order_by('parent_comment_id', 'comment_id')[offset:offset+limit]

    @staticmethod
    def find_all_infinite_scroll(article_id, last_parent_comment_id=None, last_comment_id=None, limit=10):
        query = Comment.objects.filter(article_id=article_id).order_by('parent_comment_id', 'comment_id')
        if last_parent_comment_id and last_comment_id:
            query = query.filter(parent_comment_id__gt=last_parent_comment_id, comment_id__gt=last_comment_id)
        return query[:limit]


class ArticleCommentCountRepository:

    @staticmethod
    def increase(article_id):
        obj, created = ArticleCommentCount.objects.get_or_create(article_id=article_id)
        obj.comment_count += 1
        obj.save()
        return obj.comment_count

    @staticmethod
    def decrease(article_id):
        obj = ArticleCommentCount.objects.filter(article_id=article_id).first()
        if obj and obj.comment_count > 0:
            obj.comment_count -= 1
            obj.save()
