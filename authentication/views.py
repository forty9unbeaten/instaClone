from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from .forms import LoginForm, SignupForm
from instauser.models import InstaUser

# Create your views here.
def index(request):
    return render(request, 'index.html')


class LoginView(View):
    form = LoginForm
    initial = {'key': 'value'}
    template_name = 'generic_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            user = authenticate(
                request,
                username = user_info['username'],
                password = user_info['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class SignupFormView(View):
    form = SignupForm
    initial = {'key': 'value'}
    template_name='generic_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            InstaUser.objects.create(
                username = user_info['username'],
                display_name = user_info['display_name'],
            )
            user = InstaUser.objects.last()
            user.set_password(user_info['password'])
            user.following.add(user)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        return render(request, self.template_name, {'form': self.form})