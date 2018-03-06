from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Comment
from .serializer import CommentSerializer

from django.shortcuts import render

# Create your views here.
# Lists and Creates entries of Comments.
#
# GET  comments/: return a list of Comments
# POST comments/: create a Comment
#      data = {
#          "comment" : "your comment"
#      }
# POST comments/: create a Comment
#      data = {
#          "comment" : "your comment"
#      }
class CommentList(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        content = {'status' : 'ok', 'data' : serializer.data}
        return Response(content)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {'status' : 'ok', 'data' : serializer.data}
            return Response(content)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Return a single Comment (even for anonymous users) and allows admin
# to update and delete a single Product.
#
# GET    comments/<id>/: return a Comment
# PUT    comments/<id>/: update a Comment
# DELETE comments/<id>/: delete a Comment
class CommentDetail(APIView):

    def get(self, request, id):
        comment = Comment.objects.get(id=id)
        serializer = CommentSerializer(comment, many=False)
        content = {'status' : 'ok', 'data' : serializer.data}
        return Response(content)

    def put(self, request, id):
        comment = Comment.objects.get(id=id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {'status': 'ok', 'data': serializer.data}
            return Response(content)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        comment = Comment.objects.get(id=id)
        comment.delete()
        content = {'status' : 'ok'}
        return Response(content)
