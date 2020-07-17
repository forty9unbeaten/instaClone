from django.urls import path, re_path
from comment import views

url_patterns = [
    path('add_comment/<int:post_id>', views.add_comment, name='add_comment'),
    path('profile/add_comment/<int:post_id>', views.add_comment, name='add_comment'),
    re_path(r'^delete_all/(?P<post_id>\d+)/(?P<page>\w+)', views.delete_all, name='delete_all'),
    re_path(r'^delete_comment/(?P<comment_id>\d+)/(?P<page>\w+)/(?:(?P<user_id>\d+))', views.delete_comment, name='delete_comment')
]
