from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from posts.models import Posts
from posts.serializers import PostSerializer

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        return Posts.objects.order_by('-created_at')
