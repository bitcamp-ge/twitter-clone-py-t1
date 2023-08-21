from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
# Create your models here.

class Likes(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_from_User = models.ForeignKey(User, on_delete=models.CASCADE)
    like_value = models.BooleanField(default=False)

    def __str__(self):
        pass