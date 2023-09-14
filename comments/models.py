from django.db import models
from accounts.models import User

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    object_id = models.ManyToManyField('posts.Post', related_name='posts')
    
    def __str__(self):
        
        return self.content
