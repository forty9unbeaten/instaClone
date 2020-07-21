from instauser.models import InstaUser
from instaPost.models import Post

def get_user(id):
    user = InstaUser.objects.get(id=id)
    return user


def get_posts_by_user(id):
    posts = Post.objects.filter(user=id)
    return posts