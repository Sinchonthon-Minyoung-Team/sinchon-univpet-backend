from django.db import models
from posts.models import Posts
from django.contrib.auth import get_user_model

# Create your models here.
class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     # 새로운 좋아요를 생성할 때마다 관련 게시물의 likes 값을 1 증가시킵니다.
    #     self.post.likes += 1
    #     self.post.save()
    #     super(Like, self).save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     # 좋아요를 삭제할 때 관련 게시물의 likes 값을 1 감소시킵니다.
    #     self.post.likes -= 1
    #     self.post.save()
    #     super(Like, self).delete(*args, **kwargs)