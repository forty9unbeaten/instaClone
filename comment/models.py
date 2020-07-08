from django.db import models
from instauser.models import InstaUser
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    comment = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(InstaUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comment
