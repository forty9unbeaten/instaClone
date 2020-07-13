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


@login_required(login_url='/login/')
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    user_id = comment.author.id
    if request.user == comment.author:
        comment.delete()
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def delete_all(request, post_id):
    post = Post.objects.get(id=post_id)
    user_id = post.user.id
    if request.user == post.user:
        post.comments.get_queryset().delete()
        return HttpResponseRedirect(reverse('profilePage', args=(user_id,)))
    return HttpResponseRedirect(reverse('profilePage', args=(user_id,)))
