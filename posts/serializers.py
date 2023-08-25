from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from posts.models import Posts, Comment

class PostSerializer(ModelSerializer):
    d_day = serializers.ReadOnlyField()

    class Meta:
        model = Posts
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'