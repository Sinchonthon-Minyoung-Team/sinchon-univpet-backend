from datetime import timedelta
from django.shortcuts import render, get_object_or_404

from django.db.models import Q

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

from posts.models import Posts, Comment
from posts.serializers import PostSerializer, CommentSerializer

from django.db.models import DateTimeField, ExpressionWrapper, F, fields
from django.db.models.functions import Now
from rest_framework.generics import ListAPIView

from likes.models import Like
from likes.serializers import LikeSerializer

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
    
    def get_queryset(self):
        queryset = Posts.objects.order_by('-created_at')

        # 정렬 쿼리
        order_query = self.request.query_params.get('order', None)
        if order_query:
            if order_query == 'latest':
                queryset = Posts.objects.order_by('-created_at')
            elif order_query == 'old':
                queryset = Posts.objects.order_by('created_at')
            else:
                queryset = Posts.objects.order_by('-created_at')

        # 키워드 쿼리
        keyword_query = self.request.query_params.get('keyword', None)
        if keyword_query:
            queryset = queryset.filter(
                Q(title__contains=keyword_query) | Q(content__contains=keyword_query))
            
        return queryset

@api_view(['GET'])
def sorted_post_list(request):
    queryset = Posts.objects.all()
    
    # d_day 속성을 기반으로 정렬합니다.
    sorted_queryset = sorted(queryset, key=lambda x: x.d_day if x.d_day != "End" else float('inf'))
    
    serializer = PostSerializer(sorted_queryset, many=True)
    return Response(serializer.data)

# class CommentViewSet(ModelViewSet):
#     authentication_classes = [BasicAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated,]
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         serializer.save(user = self.request.user)

@api_view(['POST'])
def add_comment(request):
    post_id = request.data.get('post_id')
    content = request.data.get('content')
    
    post = Posts.objects.get(id=post_id)
    
    comment = Comment(post=post, user=request.user, content=content)
    comment.save()
    
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)    

@api_view(['GET'])
def get_petition_detail(request, post_id):
    try:
        # Post 정보 가져오기
        post = Posts.objects.get(id=post_id)
        post_serializer = PostSerializer(post)

        # Comment 정보 가져오기
        comments = Comment.objects.filter(post=post)
        comment_serializer = CommentSerializer(comments, many=True)

        # Like 정보 가져오기
        likes = Like.objects.filter(post=post)
        like_serializer = LikeSerializer(likes, many=True)

        return Response({
            'post': post_serializer.data,
            'comments': comment_serializer.data,
            'likes': like_serializer.data
        }, status=status.HTTP_200_OK)

    except Posts.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)