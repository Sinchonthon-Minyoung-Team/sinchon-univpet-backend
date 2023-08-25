# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from likes.serializers import LikeSerializer
# from likes.models import Like
# from posts.models import Posts
# from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import IsAuthenticated
# from django.http.response import Http404
# from django.db.models import F

# likes/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from likes.models import Like
from .serializers import LikeSerializer
from posts.models import Posts
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class LikeToggle(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, post_id):
        post = get_object_or_404(Posts, id=post_id)
        user = request.user  # 현재 사용자

        try:
            like = Like.objects.get(post=post, user=user)
        except Like.DoesNotExist:
            like = None

        if like:
            # 이미 좋아요를 누른 경우, 좋아요 취소
            like.delete()
            post.likes -= 1
            post.save()
            return Response({"likes": post.likes}, status=status.HTTP_200_OK)
        else:
            # 아직 좋아요를 누르지 않은 경우, 좋아요 추가
            Like.objects.create(post=post, user=user)
            post.likes += 1
            post.save()
            return Response({"likes": post.likes}, status=status.HTTP_201_CREATED)

class LikeCountView(APIView):
    def get(self, request, post_id):
        try:
            post = Posts.objects.get(pk=post_id)
            like_count = post.likes
            return Response({"likes": like_count}, status=status.HTTP_200_OK)
        except Posts.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)