from django.shortcuts import render
from django.views.generic import View
from .models import Post

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
        

