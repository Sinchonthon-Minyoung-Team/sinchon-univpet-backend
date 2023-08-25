from django.db import models
from posts.models import Posts
from django.contrib.auth import get_user_model

# Create your models here.
class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)