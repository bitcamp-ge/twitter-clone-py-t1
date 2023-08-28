from django.db import models
from accounts.models import User
# Create your models here.

class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_message")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipient_message")
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    

    def __str__(self):
        return f"From {self.sender} to {self.recipient} at {self.timestamp}"