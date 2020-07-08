from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('signup/', views.SignupFormView.as_view(), name='signup')
]