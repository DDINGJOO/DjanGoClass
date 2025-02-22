from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import CommentService
from .serializers import CommentCreateRequest

class CommentView(APIView):

    def post(self, request):
        serializer = CommentCreateRequest(data=request.data)
        if serializer.is_valid():
            response_data = CommentService.create(serializer.validated_data)
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, comment_id=None):
        if comment_id:
            return Response(CommentService.read(comment_id), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        CommentService.delete(comment_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
