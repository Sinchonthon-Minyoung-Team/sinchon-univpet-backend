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
        # # 사용자가 해당 게시물에 대한 좋아요를 이미 눌렀는지 확인
        # existing_like = Like.objects.filter(post=post, user=user).first()

        # if existing_like:
        #     # 이미 좋아요를 눌렀다면 좋아요 삭제
        #     existing_like.delete()
        #     liked = False
        # else:
        #     # 좋아요를 누르지 않았다면 좋아요 생성
        #     Like.objects.create(post=post, user=user)
        #     liked = True

        # # 좋아요 토글 결과 반환
        # return Response({'liked': liked})



#class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

# class LikeDetail(generics.RetrieveAPIView, generics.CreateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     #permission_classes = [IsAuthenticated]
#     lookup_field = 'post'

#     def get_filter_kwargs(self):
#         """
#         Returns the keyword arguments that can be used as a filter. 
        
#         Output:
#             {
#                 'post': the related Post object
#                 'user': the request user
#             }
        
#         May throw 404 if post doesn't exists
#         """
#         filter_kwargs = {}
        
#         lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

#         assert lookup_url_kwarg in self.kwargs, (
#             'Expected view %s to be called with a URL keyword argument '
#             'named "%s". Fix your URL conf, or set the `.lookup_field` '
#             'attribute on the view correctly.' %
#             (self.__class__.__name__, lookup_url_kwarg)
#         )

#         post = get_object_or_404(Posts.objects.all(), id=self.kwargs[lookup_url_kwarg])
#         filter_kwargs[self.lookup_field] = post
#         filter_kwargs['user'] = self.request.user

#         return filter_kwargs

#     def get_object(self):
#         """
#         Returns the object that satisfies the following conditions:
#             1) the view is displaying
#             2) the requested user is the 'user'

#         If user didn't like -> None
#         If permission denied -> 404
#         """

#         queryset = self.filter_queryset(self.get_queryset())

#         filter_kwargs = self.get_filter_kwargs()
#         try: 
#             obj = get_object_or_404(queryset, **filter_kwargs)
#         except Http404: 
#             return None

#         # May raise a permission denied
#         self.check_object_permissions(self.request, obj)

#         return obj

#     def retrieve(self, request, *args, **kwargs):
#         """
#         Gives 200 if the requested user liked the post number
#         Gives 204 if the requested user didn't like the post number
#         Else, gives 404
#         """

#         like_obj = self.get_object()
#         if like_obj is not None:
#             return Response(status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)
        
    
#     def create(self, request, *args, **kwargs):
#         like_instance = self.get_object()
#         if like_instance is not None:
#             # 이미 좋아요를 누른 경우 좋아요 취소
#             like_instance.delete()
#             post = self.get_filter_kwargs()['post']
#             post.likes = F('likes') - 1
#             post.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)

#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)

#         post = self.get_filter_kwargs()['post']
#         post.likes = F('likes') + 1
#         post.save()

#         headers = self.get_success_headers(serializer.data)
#         return Response(status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         filter_kwargs = self.get_filter_kwargs()
#         serializer.save(**filter_kwargs)
    
#     def destroy(self, request, *args, **kwargs):
#         like_instance = self.get_object()
#         if like_instance is not None:
#             post = self.get_filter_kwargs()['post']
#             post.likes = F('likes') - 1
#             post.save()

#         like_instance.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)