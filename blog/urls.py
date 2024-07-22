from django.urls import path
from .views import (
    home, login_view, signup_view, post_list_view, post_detail, create_post, edit_post, add_comment, logout_view, update_post, delete_post
)
from .api.views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, api_login

urlpatterns = [
    # Home Page
    path('', home, name='home'),

    # User Authentication
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),

    # Post Management
    path('create_post/', create_post, name='create_post'),
    path('posts/', post_list_view, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/<int:pk>/edit/', edit_post, name='edit-post'),
    path('posts/<int:pk>/update/', update_post, name='update-post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete-post'),

    # Comments
    path('posts/<int:post_id>/add_comment/', add_comment, name='add-comment'),

    # API Endpoints
    path('api/posts/', PostListCreateView.as_view(), name='api-post-list-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='api-post-detail'),
    path('api/posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='api-comment-list-create'),
    path('api/login/', api_login, name='api_login'),
]
