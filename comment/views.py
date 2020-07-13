from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from instaPost.models import Post
from comment.models import Comment

# Create your views here.


@login_required(login_url='/login/')
def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        new_comment = Comment(
            comment=request.POST['comment'],
            author=request.user)
        new_comment.save()
        post.comments.add(new_comment)
        return HttpResponseRedirect(reverse('home'))
