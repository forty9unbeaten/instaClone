from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:id>', views.profilePage, name='profilePage'),
    path('follow/<int:id>/', views.follow, name='follow'),
    path('editprofile/edit/<int:id>', views.EditProfile, name='edit'),
    path('unfollow/<int:id>/', views.unfollow, name='unfollow')
]