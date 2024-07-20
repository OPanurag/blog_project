"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

from blog_project.blog.views import login_view, signup_view, post_list_view, post_detail, create_post, edit_post
from blog_project.blog.views import PostListCreateView, CommentListCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('create_post/', create_post, name='create_post'),
    path('posts/add/', create_post, name='create-post'),
    path('posts/<int:pk>/edit/', edit_post, name='edit-post'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/', post_list_view, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
]
