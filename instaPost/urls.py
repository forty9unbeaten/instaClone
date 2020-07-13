from django.urls import path
from . import views

url_patterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('newpost/', views.newpost, name='newPost'),
    path('like/<int:post_id>', views.like_post, name='like'),
    path('unlike/<int:post_id>', views.unlike_post, name='unlike')
]
