from django.shortcuts import render, reverse, HttpResponseRedirect
from instauser.models import InstaUser
from django.contrib.auth import login, authenticate
from instaPost.models import Post
from authentication.forms import SignupForm

# Create your views here.


def profilePage(request, id):
    try:
        user = InstaUser.objects.get(id=id)
    except:
        # user can't be found with ID provided in URL
        return render(
            request,
            'error.html',
            {
                'code': '404'
            })

    posts = Post.objects.filter(user=id).filter(archived=False)
    countposts = posts.count()
    followers = user.following.all()
    countfollowers = followers.count() - 1
    if request.user.is_authenticated:
        myfollowers = request.user.following.all()
        if request.user in followers:
            is_following = True
        else:
            is_following = False
        return render(
            request,
            'profilePage.html', {
                'posts': posts,
                'countposts': countposts,
                'user': user,
                'countfollowers': countfollowers,
                'myfollowers': myfollowers,
                'is_following': is_following,
            })
    return render(
        request,
        'profilePage.html', {
            'posts': posts,
            'countposts': countposts,
            'user': user,
            'countfollowers': countfollowers,
        })


def EditProfile(request, id):

    try:
        user = InstaUser.objects.get(id=id)
    except:
        return render(
            request,
            'error.html',
            {
                'code': '404'
            }
        )

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.display_name = data['display_name']
            user.bio = data['bio']
            user.email = data['email']
            user.save()
        return HttpResponseRedirect(reverse('profilePage', args=(id,)))
    form = SignupForm(initial={
        'display_name': user.display_name,
        'bio': user.bio,
        'email': user.email,
    })
    return render(request, 'generic_form.html', {'form': form})


def follow(request, id):
    try:
        follow = InstaUser.objects.get(id=id)
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


def unfollow(request, id):
    try:
        follow = InstaUser.objects.get(id=id)
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
