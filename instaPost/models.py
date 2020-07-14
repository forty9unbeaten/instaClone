from django.db import models
from comment.models import Comment
from instauser.models import InstaUser

# Create your models here.


class Post(models.Model):
    picture = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=140, null=True, blank=True)
    user = models.ForeignKey(InstaUser,
                             on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment, blank=True)
    likes = models.ManyToManyField(
        InstaUser, blank=True, related_name='post_likes')
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.caption
