import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from comment.models import Comment, ArticleCommentCount


@pytest.mark.django_db

## Given : 준비물
## When : 작동하고
## Then : 그래서?
class TestCommentCreateAPI:
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

        ArticleCommentCount.objects.create(article_id=self.article_id, comment_count=1)

    def test_create_parent_comment(self):
        """부모 댓글을 정상적으로 생성하는지 테스트"""
        url = reverse("create_comment")
        data = {
            "article_id": self.article_id,
            "content": "새로운 부모 댓글",
            "parent_comment_id": None,
            "writer_id": self.writer_id,
        }
        ## Given
        response = self.client.post(url, data, format="json")
        ## When

        ##then
        assert response.status_code == 201
        assert response.data["content"] == "새로운 부모 댓글"
        assert response.data["parent_comment_id"] is None

    def test_create_child_comment(self):
        """부모 댓글이 존재하는 경우, 자식 댓글을 생성하는 테스트"""
        url = reverse("create_comment")
        data = {
            "article_id": self.article_id,
            "content": "자식 댓글입니다.",
            "parent_comment_id": self.parent_comment.comment_id,
            "writer_id": self.writer_id,
        }
        response = self.client.post(url, data, format="json")

        assert response.status_code == 201
        assert response.data["content"] == "자식 댓글입니다."
        assert response.data["parent_comment_id"] == self.parent_comment.comment_id



    def test_create_comment_with_nonexistent_parent(self):
        """존재하지 않는 부모 댓글 ID를 지정하면 400 오류를 반환하는지 테스트"""
        url = reverse("create_comment")
        data = {
            "article_id": self.article_id,
            "content": "잘못된 부모 댓글을 가진 댓글",
            "parent_comment_id": 9999,  # 존재하지 않는 부모 댓글 ID
            "writer_id": self.writer_id,
        }
        response = self.client.post(url, data, format="json")

        assert response.status_code == 400
        assert "parent_comment_id" in response.data  # 올바르지 않은 부모 댓글 에러 확인

    def test_create_nested_child_comment(self):
        """자식 댓글이 있는 댓글에 추가로 자식 댓글을 생성하는 테스트"""
        # 첫 번째 자식 댓글 생성
        first_child = Comment.objects.create(
            content="첫 번째 자식 댓글",
            article_id=self.article_id,
            writer_id=self.writer_id,
            parent_comment_id=self.parent_comment.comment_id
        )

        url = reverse("create_comment")
        data = {
            "article_id": self.article_id,
            "content": "두 번째 자식 댓글",
            "parent_comment_id": first_child.comment_id,  # 첫 번째 자식 댓글을 부모로 지정
            "writer_id": self.writer_id,
        }
        response = self.client.post(url, data, format="json")

        assert response.status_code == 201
        assert response.data["content"] == "두 번째 자식 댓글"
        assert response.data["parent_comment_id"] == first_child.comment_id
