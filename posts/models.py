from django.db import models 
from accounts.models import User
from hashtags.models import Hashtag

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content