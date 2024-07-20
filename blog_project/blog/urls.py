from django.urls import path
from .views import (
    login_view,
    signup_view,
    create_post,
    edit_post,  # Make sure to add this view in your views.py
    post_list_view,
    post_detail,
    add_comment,  # Make sure to add this view in your views.py
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    CommentListCreateView
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),

    # Combined post creation path
    path('posts/add/', create_post, name='create-post'),

    # Post edit view
    path('posts/<int:pk>/edit/', edit_post, name='edit-post'),

    # Post detail view
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),

    # Comment-related views
    path('posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/<int:post_id>/add-comment/', add_comment, name='add-comment'),  # URL for adding a new comment

    # Post list view (for the HTML view)
    path('posts/html/', post_list_view, name='post-list-html'),

    # Post detail view (for the HTML view)
    path('posts/<int:pk>/html/', post_detail, name='post-detail-html'),
]
