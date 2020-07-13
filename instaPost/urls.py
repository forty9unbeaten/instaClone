from django.urls import path
from . import views

url_patterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('newpost/', views.newpost, name='newPost'),
    path('like/<int:post_id>', views.like_post, name='like'),
    path('unlike/<int:post_id>', views.unlike_post, name='unlike'),
    path('post/<id>/delete/', views.delete_post, name='delete_post'),
    path('archive/<int:id>/', views.archive_post, name='archive'),
    path('unarchive/<int:id>/', views.unarchive_post, name='unarchive'),
    path('archived-posts/<int:id>', views.archived_posts, name='archived_posts')
]
