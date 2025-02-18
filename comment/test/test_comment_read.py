import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from comment.models import Comment, ArticleCommentCount


@pytest.mark.django_db
class TestCommentReadAPI:
    def setup_method(self):
        """각 테스트 실행 전 기본 데이터 생성"""
        self.client = APIClient()
        self.article_id = 1
        self.writer_id = 1001

        # 부모 댓글 생성
        self.parent_comment = Comment.objects.create(
            content="부모 댓글입니다.",
            article_id=self.article_id,
            writer_id=self.writer_id,
            parent_comment_id=None
        )

        # 자식 댓글 생성
        self.child_comment = Comment.objects.create(
            content="자식 댓글입니다.",
            article_id=self.article_id,
            writer_id=self.writer_id,
            parent_comment_id=self.parent_comment.comment_id
        )

        # 댓글 개수 카운트
        ArticleCommentCount.objects.create(article_id=self.article_id, comment_count=2)

    def test_read_single_comment(self):
        """단일 댓글을 조회할 수 있는지 테스트"""
        url = reverse("manage_comment", args=[self.parent_comment.comment_id])
        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data["content"] == "부모 댓글입니다."
        assert response.data["parent_comment_id"] is None

    def test_read_comment_list(self):
        """특정 게시글(article_id)의 모든 댓글을 계층적으로 조회할 수 있는지 테스트"""
        url = reverse("create_comment") + f"?article_id={self.article_id}"
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.data["comments"]) == 2  # 부모 + 자식 댓글

        parent_comment = next(c for c in response.data["comments"] if c["comment_id"] == self.parent_comment.comment_id)
        child_comment = next(c for c in response.data["comments"] if c["comment_id"] == self.child_comment.comment_id)

        assert parent_comment["content"] == "부모 댓글입니다."
        assert child_comment["content"] == "자식 댓글입니다."
        assert child_comment["parent_comment_id"] == self.parent_comment.comment_id

    def test_read_comment_pagination(self):
        """페이징 처리가 정상적으로 동작하는지 테스트"""
        # 추가 댓글 생성 (총 15개)
        for i in range(15):
            Comment.objects.create(
                content=f"테스트 댓글 {i}",
                article_id=self.article_id,
                writer_id=self.writer_id,
                parent_comment_id=None
            )

        url = reverse("create_comment") + f"?article_id={self.article_id}&page=1&page_size=10"
        response = self.client.get(url)

        assert response.status_code == 200
        assert len(response.data["comments"]) == 10  # 페이지 크기가 10이므로 10개만 조회됨

    def test_read_deleted_comment(self):
        """삭제된 댓글이 조회되지 않는지 테스트 (Soft Delete)"""
        self.parent_comment.deleted = True
        self.parent_comment.save()

        url = reverse("manage_comment", args=[self.parent_comment.comment_id])
        response = self.client.get(url)

        assert response.status_code == 404  # Soft Delete 처리된 댓글은 조회 불가능해야 함
