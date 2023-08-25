from django.shortcuts import render
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from posts.models import Posts
from posts.serializers import PostSerializer

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
