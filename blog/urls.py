from django.urls import path
from .views import (
    home, login_view, signup_view, post_list_view, post_detail, create_post, edit_post, add_comment, logout_view, update_post, delete_post
)
from .api.views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, api_login

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('create_post/', create_post, name='create-post'),
    path('posts/', post_list_view, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/<int:pk>/edit/', edit_post, name='edit-post'),
    path('posts/<int:post_id>/add_comment/', add_comment, name='add-comment'),

    path('posts/<int:post_id>/update/', update_post, name='update_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),


    # API endpoints
    path('api/posts/', PostListCreateView.as_view(), name='api-post-list-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='api-post-detail'),
    path('api/posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='api-comment-list-create'),
    path('api/login/', api_login, name='api_login'),
]
