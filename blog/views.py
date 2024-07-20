# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics

from .forms import PostForm
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_pk = self.kwargs['post_pk']
        return Comment.objects.filter(post_id=post_pk)

    def perform_create(self, serializer):
        post_pk = self.kwargs['post_pk']
        post = Post.objects.get(pk=post_pk)
        serializer.save(post=post)


def home(request):
    return render(request, 'home.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list-create')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form})
