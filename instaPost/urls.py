from django.urls import path, re_path
from . import views

url_patterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('discover/', views.DiscoverPageView.as_view(), name='discover'),
    path('newpost/', views.newpost, name='newPost'),
    path('like/<int:post_id>/<str:page>', views.like_post, name='like'),
    path('unlike/<int:post_id>/<str:page>', views.unlike_post, name='unlike'),
    re_path(r'^post/(?P<id>\d+)/delete/(?P<page>\w+)',
            views.delete_post, name='delete_post'),
    path('archive/<int:id>/', views.archive_post, name='archive'),
    path('unarchive/<int:id>/', views.unarchive_post, name='unarchive'),
    path('archived-posts/<int:id>', views.archived_posts, name='archived_posts')
]
