from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, reverse
from instaPost.models import Post
from comment.models import Comment

# Create your views here.


@login_required
def add_comment(request, post_id, page):
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
        if page == 'profilePage':
            return HttpResponseRedirect(reverse(page, args=(post.user.id,)))
        return HttpResponseRedirect(reverse(page))


@login_required
def delete_comment(request, comment_id, page, user_id):
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
    if page == 'profilePage':
        return HttpResponseRedirect(reverse(page, args=(user_id,)))
    return HttpResponseRedirect(reverse('home'))


@login_required
def delete_all(request, post_id, page):
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
        if page == 'profilePage':
            return HttpResponseRedirect(reverse('profilePage', args=(user_id,)))
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('profilePage', args=(user_id,)))
