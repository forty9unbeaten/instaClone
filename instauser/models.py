from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class InstaUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='follow')

    REQUIRED_FIELDS = ['display_name']
