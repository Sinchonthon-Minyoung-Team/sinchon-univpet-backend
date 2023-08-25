from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from posts.models import Posts

class PostSerializer(ModelSerializer):
    status = serializers.ReadOnlyField()

    class Meta:
        model = Posts
        fields = '__all__'
