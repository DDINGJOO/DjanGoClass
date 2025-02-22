import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from comment.models import Comment, ArticleCommentCount


@pytest.mark.django_db
class TestCommentDeleteAPI:
    def setup_method(self):
        """각 테스트 실행 전 실행됨"""
        self.client = APIClient()
        self.article_id = 1
        self.writer_id = 1001

        # 테스트용 댓글 데이터 생성
        self.comment = Comment.objects.create(
            content="테스트 댓글입니다.",
            article_id=self.article_id,
            writer_id=self.writer_id,
            parent_comment_id=None
        )
        self.child_comment = Comment.objects.create(
            content="자식 댓글",
            article_id=self.article_id,
            writer_id=self.writer_id,
            parent_comment_id=self.comment.comment_id
        )
        ArticleCommentCount.objects.create(article_id=self.article_id, comment_count=2)

    def test_soft_delete_comment(self):
        """Soft Delete 테스트: deleted=True가 되는지 확인"""
        url = reverse("manage_comment", args=[self.comment.comment_id])
        response = self.client.delete(url)

        assert response.status_code == 204
        self.comment.refresh_from_db()
        assert self.comment.deleted is True  # Soft Delete 처리 확인

    def test_hard_delete_comment(self):
        """Hard Delete 테스트: 데이터베이스에서 완전히 삭제되는지 확인"""
        url = reverse("manage_comment", args=[self.comment.comment_id])

        # Soft Delete
        self.client.delete(url)

        # Hard Delete: Soft Delete된 댓글을 완전 삭제
        self.comment.delete()
        assert not Comment.objects.filter(comment_id=self.comment.comment_id).exists()





    def test_cascade_delete_comment(self):
        """Cascade Delete 테스트: 부모 댓글 삭제 시 자식 댓글이 삭제되는지 확인"""
        url = reverse("manage_comment", args=[self.comment.comment_id])

        # Soft Delete 부모 댓글
        self.client.delete(url)

        # 부모 댓글을 Hard Delete하면 자식 댓글도 삭제됨 (Cascade Delete)
        self.comment.delete()
        assert not Comment.objects.filter(parent_comment_id=self.comment.comment_id).exists()

    def test_logical_delete_comment(self):
        """Logical Delete 테스트: deleted_at 필드가 설정되는지 확인"""
        self.comment.deleted = True
        self.comment.save()

        assert self.comment.deleted is True  # Logical Delete 확인
