from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture =models.ImageField()
    followers = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.user.username