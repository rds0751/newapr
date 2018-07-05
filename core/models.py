from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Organization(models.Model):
	oname = models.CharField(max_length=250,default='')

	def __str__(self):
		return self.oname

class UserProfile(models.Model):
    RIO = (('','Select your Role in Organization'),
    ('executive', 'Executive'),
    ('admin', 'Admin'),
    ('student', 'Student'),)
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    oid=models.ForeignKey(Organization, on_delete=models.CASCADE, default='')
    rio=models.CharField(max_length=20,default='',choices=RIO)

    def __str__(self):
        return self.user.first_name
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

