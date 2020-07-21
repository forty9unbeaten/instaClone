from django.shortcuts import render, reverse, HttpResponseRedirect
from instauser.models import InstaUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from instaPost.models import Post
from authentication.forms import SignupForm
from instauser.helpers import get_user, get_posts_by_user

# Create your views here.


def profilePage(request, id):
    try:
        user = get_user(id)
    except:
        # user can't be found with ID provided in URL
        return render(
            request,
            'error.html',
            {
                'code': '404'
            })
    context = {}
    context['user'] = user
    posts = get_posts_by_user(id).filter(archived=False)
    context['posts'] = posts
    context['countposts'] = posts.count()
    followers = user.following.all()
    context['countfollowers'] = followers.count() - 1
    if request.user.is_authenticated:
        context['myfollowers'] = request.user.following.all()
        if request.user in followers:
            context['is_following'] = True
        else:
            context['is_following'] = False
        return render(
            request,
            'profilePage.html', context)
    return render(
        request,
        'profilePage.html', context)


@login_required
def EditProfile(request, id):

    try:
        user = get_user(id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    if user == request.user:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user.display_name = data['display_name']
                user.bio = data['bio']
                user.email = data['email']
                user.url = data['url']
                user.save()
            return HttpResponseRedirect(reverse('profilePage', args=(id,)))
        form = SignupForm(initial={
            'username': user.username,
            'display_name': user.display_name,
            'bio': user.bio,
            'email': user.email,
            'url': user.url
        })
        return render(request, 'generic_form.html', {'form': form})
    return HttpResponseRedirect(reverse('profilePage', args=(id,)))

@login_required
def follow(request, id):
    try:
        follow = get_user(id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    user = request.user
    follow.following.add(user)
    follow.save()
    return HttpResponseRedirect(reverse('profilePage', args={id, }))

@login_required
def unfollow(request, id):
    try:
        follow = get_user(id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )
    user = request.user
    follow.following.remove(user)
    follow.save()
    return HttpResponseRedirect(reverse('profilePage', args={id, }))
