from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Post, Comment
from .forms import PostForm, CommentForm
from .forms import CustomUserCreationForm


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)  # Ensure Comment is used here
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post_id)

    return redirect('post-detail', pk=post_id)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a page after login
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    return Response({'error': 'Invalid credentials'}, status=400)


# @login_required
# def home(request):
#     user = request.user
#     posts = Post.objects.all()
#     form = PostForm()  # Add this line to pass the form to the template
#     return render(request, 'blog/home.html', {'user': user, 'posts': posts, 'form': form})

def home(request):
    posts = Post.objects.all()
    user_logged_in = request.user.is_authenticated
    return render(request, 'blog/home.html', {
        'posts': posts,
        'user_logged_in': user_logged_in,
    })


def logout_view(request):
    auth_logout(request)
    return redirect('home')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author field
            post.save()
            return redirect('post-list')  # Redirect to post list after saving
    else:
        form = PostForm()

    context = {
        'form': form,
        'form_title': 'Add New Post',
        'button_text': 'Add Post'
    }
    return render(request, 'blog/post_form.html', context)


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})









