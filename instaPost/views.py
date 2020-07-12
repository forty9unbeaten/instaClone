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

def like(request, post_id):
    current_user = request.user
    image=Post.objects.get(id=post_id)
    new_like,created= Likes.objects.get_or_create(liker=current_user, image=image)
    new_like.save()

    return redirect('home')


def new_like(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewLikeForm(request.POST)
       
        post = request.POST['post']
        user = request.POST['user']
        like = Like.objects.filter(post=post, user=user)

        #import pdb; pdb.set_trace()
        # check whether it's valid:
        if like:
            like.delete()
            return redirect(request.META.get('HTTP_REFERER'))
        elif form.is_valid():
            form.save()
            # redirect to a new URL:
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        # if a GET (or any other method) we'll create a blank form
        form = NewLikeForm()
    