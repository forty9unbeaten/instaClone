from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from instaPost.models import Post
from comment.models import Comment

# Create your views here.


@login_required(login_url='/login/')
def add_comment(request, post_id):
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)
        except:
            return render(
                request,
                'error.html',
                {
                    'code': '404'
                }
            )
        new_comment = Comment(
            comment=request.POST['comment'],
            author=request.user)
        new_comment.save()
        post.comments.add(new_comment)
        return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    comment.delete()
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def delete_all(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    user_id = post.user.id
    if request.user == post.user:
        post.comments.get_queryset().delete()
        return HttpResponseRedirect(reverse('profilePage', args=(user_id,)))
    return HttpResponseRedirect(reverse('profilePage', args=(user_id,)))
