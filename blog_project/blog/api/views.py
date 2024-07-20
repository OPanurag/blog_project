# blog/api/views.py
from rest_framework import generics
from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_id)
