from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser
from posts.models import Posts

class UserProfileView(APIView):
    def get(self, request, user_id):
        user_profile = get_object_or_404(CustomUser, id=user_id)

        post_ids = Posts.objects.filter(writer=user_profile).values_list('id', flat=True)

        data = {
            'username': user_profile.username,
            'name': user_profile.name,
            'university': user_profile.university,
            'major': user_profile.major,
            'post_ids': list(post_ids),
        }
        return Response(data, status=status.HTTP_200_OK)
