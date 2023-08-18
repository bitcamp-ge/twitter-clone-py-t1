from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    

    def __str__(self):
        return f"From {self.sender} to {self.recipient} at {self.timestamp}"