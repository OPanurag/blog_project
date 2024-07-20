from django.urls import path
from .views import (
    login_view, signup_view, post_list_view, post_detail, create_post, edit_post, add_comment
)
from .api.views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView

urlpatterns = [
    # Standard Django views
    path('', post_list_view, name='home'),  # Redirect to a view to avoid 404 on root
    path('posts/', post_list_view, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/add/', create_post, name='create-post'),
    path('posts/<int:pk>/edit/', edit_post, name='edit-post'),
    path('posts/<int:post_id>/add_comment/', add_comment, name='add-comment'),

    # API endpoints using Django REST Framework
    path('api/posts/', PostListCreateView.as_view(), name='api-post-list-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='api-post-detail'),
    path('api/posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='api-comment-list-create'),

    # Authentication
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
