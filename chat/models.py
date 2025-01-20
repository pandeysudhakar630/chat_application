from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(
        User,
        related_name='sent_messages',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name='received_messages',
        on_delete=models.CASCADE
    )
    content = models.TextField()  # Message content
    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-filled timestamp

    def __str__(self):
        """
        String representation of the Message model.
        Displays the sender, receiver, timestamp, and a preview of the content.
        """
        return f'{self.sender.username} to {self.receiver.username} at {self.timestamp}: {self.content[:20]}'
