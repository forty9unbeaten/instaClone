"""instaClone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from instaClone import settings
from authentication.urls import urlpatterns as authurls
from instauser.urls import urlpatterns as userurls
from instaPost.urls import url_patterns as post_urls
from comment.urls import url_patterns as comment_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += authurls
urlpatterns += userurls
urlpatterns += post_urls
urlpatterns += comment_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
