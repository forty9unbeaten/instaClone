from django.urls import path
from comment import views

url_patterns = [
    path('add_comment/<int:post_id>', views.add_comment, name='add_comment'),
    path('delete_all/<int:post_id>', views.delete_all, name='delete_all'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment')
]
