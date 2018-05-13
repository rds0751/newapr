from django.contrib.auth.models import User
from django.db import models

from core.models import UserProfile

up = UserProfile.objects.all()
execList = []
for i in up:
    if i.rio == 'executive':
        us = []
        user = User.objects.get(first_name=i.user.first_name)
        us.append(user)
        us.append(user)
        execList.append(us)

class Document(models.Model):
    executive = models.ForeignKey(User, on_delete=models.CASCADE, choices=execList)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
