from django.db import models
from accounts.models import User
from posts.models import Post

class Likes(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_id', blank=True, null=True)
    like_from_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_Like', blank=True, null=True)
    like_value = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.like_from_User} likes {self.postId}"