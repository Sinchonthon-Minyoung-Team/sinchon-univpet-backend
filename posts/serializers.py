from rest_framework.serializers import ModelSerializer

from posts.models import Posts

class PostSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        