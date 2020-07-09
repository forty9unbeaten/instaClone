from django.shortcuts import render, reverse, HttpResponseRedirect
from instauser.models import InstaUser
from django.contrib.auth import login, authenticate
from instaPost.models import Post


# Create your views here.

def profilePage(request, id):
    posts = Post.objects.filter(user=id)
    countposts = posts.count()
    user = InstaUser.objects.get(id=id)
    followers = user.following.all()
    countfollowers = followers.count()
    if request.user.is_authenticated:
        myfollowers = request.user.following.all()
        if user in myfollowers:
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
    
def follow(request, id):
    user = request.user
    follow = InstaUser.objects.get(id=id)
    user.following.add(follow)
    user.save()
    return HttpResponseRedirect(reverse('profilePage', args={id,}))

def unfollow(request, id):
    user = request.user
    follow = InstaUser.objects.get(id=id)
    user.following.remove(follow)
    user.save()
    return HttpResponseRedirect(reverse('profilePage', args={id,}))