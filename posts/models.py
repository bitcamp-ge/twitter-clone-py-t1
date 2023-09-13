from django.db import models 
from accounts.models import User
from hashtags.models import Hashtag
from likes.models import Likes
from comments.models import Comment

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, related_name='posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through=Likes, related_name='post_likes')
    comments = models.ManyToManyField(Comment, related_name='post_comments')
   
    def __str__(self):
        return self.content
    

    

   