from django.db import models
from django.conf import settings

# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    msg = models.CharField(max_length=1000)
    sent_at = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return f'mensagem de {self.user.username} às {self.sent_at}'


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feedback')
    feedback = models.TextField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_feedback', blank=True)
    submitted_at = models.TimeField(auto_now_add=True)

    def feedback_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return f'feedback de {self.user.username} às {self.submitted_at}'

    class Meta:
        ordering = ['-submitted_at']

