# blog/urls.py
from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDelete, CommentListCreate, home, post_list, post_detail, post_create, post_update

urlpatterns = [
    path('', home, name='home'),
    path('posts/', post_list, name='post-list-create'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/create/', post_create, name='post-create'),
    path('posts/<int:pk>/update/', post_update, name='post-update'),
    path('posts/<int:post_pk>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
