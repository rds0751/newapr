from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from core.models import UserProfile



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Ticket(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='haw')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title