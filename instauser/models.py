from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class InstaUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='follow')
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=150)
    url = models.URLField(blank=True)

    REQUIRED_FIELDS = ['display_name', 'email']
