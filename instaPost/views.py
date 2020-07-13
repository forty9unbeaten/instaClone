from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import NewPostForm

# Create your views here.


class HomepageView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(
            request,
            'index.html',
            {
                'posts': posts
            })


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
        post = Post.objects.get(id=post_id)
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('home'))


@login_required(login_url='/login/')
def unlike_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.likes.remove(request.user)
        return HttpResponseRedirect(reverse('home'))
