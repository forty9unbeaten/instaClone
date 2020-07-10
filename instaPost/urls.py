from django.urls import path
from . import views

url_patterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('newpost/', views.newpost, name='newPost'),
    path('like/<int:post_id>/', views.likepost, name='like'),
]
