from django.db import models
from django.utils.timezone import now


class ArticleCommentCount(models.Model):
    article_id = models.BigIntegerField(primary_key=True)
    comment_count = models.BigIntegerField(default=1)

    @classmethod
    def init(cls, article_id):
        return cls(article_id=article_id, comment_count=1)


class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    content = models.TextField()
    parent_comment_id = models.BigIntegerField(null=True, blank=True)
    article_id = models.BigIntegerField()
    writer_id = models.BigIntegerField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)

    @classmethod
    def create(cls, content, parent_comment_id, article_id, writer_id):
        parent_id = parent_comment_id if parent_comment_id else None
        return cls(content=content, parent_comment_id=parent_id, article_id=article_id, writer_id=writer_id)

    def is_root(self):
        return self.parent_comment_id is None

    def delete_comment(self):
        self.deleted = True
        self.save()
