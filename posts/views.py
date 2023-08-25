from datetime import timedelta
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from posts.models import Posts
from posts.serializers import PostSerializer

from django.db.models import DateTimeField, ExpressionWrapper, F
from django.db.models.functions import Now
from rest_framework.generics import ListAPIView

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)
    
    def get_queryset(self):
        return Posts.objects.order_by('-created_at')
    
class SortedPostListView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Posts.objects.all()
        queryset = queryset.annotate(
            expire_at=ExpressionWrapper(
                F('created_at') + timedelta(days=1) * F('duration'),
                output_field=DateTimeField()
            )
        )
        
        queryset = sorted(queryset, key=lambda x: x.expire_at)  # 만료 시간을 기준으로 정렬
        return queryset
