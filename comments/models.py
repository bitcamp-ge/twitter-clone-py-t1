from django.db import models
from posts.models import Post
from accounts.models import User

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    object_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        
        return self.content