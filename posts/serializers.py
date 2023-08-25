from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from posts.models import Posts

class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['writer', 'title', 'category', 'content', 'created_at', 'd_day', 'duration']
