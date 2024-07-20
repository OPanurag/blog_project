from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import views
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, home, post_detail

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Change to JWT view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('', views.home, name='home'),

    path('create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('api/posts/', views.PostListCreateView.as_view(), name='api_post_list_create'),
    path('api/posts/<int:pk>/', views.PostRetrieveUpdateDestroyView.as_view(), name='api_post_detail'),
    path('api/posts/<int:post_pk>/comments/', views.CommentListCreateView.as_view(), name='api_comment_list_create'),
    path('api/login/', views.login, name='api_login'),

    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
