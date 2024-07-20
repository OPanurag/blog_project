from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDelete, CommentListCreate

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDelete.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
