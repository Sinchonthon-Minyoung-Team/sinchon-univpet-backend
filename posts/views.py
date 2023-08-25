from django.shortcuts import render, get_object_or_404


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from posts.models import Posts
from posts.serializers import PostSerializer

from django.http import HttpResponse

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    #permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer(writer=self.request.user).save()
    
    def get_queryset(self):
        return Posts.objects.order_by('-created_at')
    
def post_detail(request, post_id):
    try:
        post = Posts.objects.get(pk=post_id)
        response_text = f"게시글 ID: {post.id}, 제목: {post.title}, 내용: {post.content}, 좋아요: {post.likes}"
        return HttpResponse(response_text)
    except Posts.DoesNotExist:
        return HttpResponse("해당 게시글을 찾을 수 없습니다.", status=404)
    
