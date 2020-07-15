from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.decorators import login_required
from .models import Post
from instauser.models import InstaUser
from .forms import NewPostForm

# Create your views here.


class HomepageView(View):
    def get(self, request):
        posts = Post.objects.filter(archived=False)
        if request.user.is_authenticated:
            posts = posts.filter(user__in=request.user.following.all())
        return render(
            request,
            'index.html',
            {
                'posts': posts
            })


class DiscoverPageView(View):
    def get(self, request):
        posts = Post.objects.filter(archived=False)
        if request.user.is_authenticated:
            posts = posts.exclude(user__in=request.user.following.all())
        return render(request, 'index.html', {'posts': posts})


@login_required(login_url='/login/')
def newpost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('home'))

    form = NewPostForm()
    return render(request, 'postUploadForm.html', {'form': form})


@login_required(login_url='/login/')
def like_post(request, post_id):
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
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def unlike_post(request, post_id):
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
        post.likes.remove(request.user)
        return HttpResponseRedirect(reverse('home'))


def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    post.delete()
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def archive_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    post.archived = True
    post.save()
    return HttpResponseRedirect(reverse('profilePage', args=(post.user.id,)))


@login_required(login_url='/login/')
def unarchive_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    post.archived = False
    post.save()
    return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def archived_posts(request, id):
    posts = Post.objects.filter(user_id=id).filter(archived=True)
    return render(request, 'index.html', {'posts': posts})
