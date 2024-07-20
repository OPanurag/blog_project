from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, CommentListCreateView, home, post_detail, login

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Change to JWT view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', home, name='home'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
]