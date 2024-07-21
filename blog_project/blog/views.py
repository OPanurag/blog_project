from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .forms import CustomUserCreationForm, PostForm
from .models import Post, Comment


def home(request):
    try:
        template = get_template('blog/home.html')
    except TemplateDoesNotExist:
        return HttpResponse("Template blog/home.html does not exist")

    posts = Post.objects.all()
    return render(request, 'blog/home.html', context={'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author field
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form, 'form_title': 'Add New Post', 'button_text': 'Add Post'})


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(post=post, author=request.user, text=text)
        return redirect('home')
    return HttpResponse("Invalid request")


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post_detail.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Use auth_login to avoid conflict
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


@api_view(['POST'])
def api_login(request):
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


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def logout_view(request):
    auth_logout(request)
    return redirect('home')


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
    return render(request, 'blog/create_post.html', {'form': form, 'post': post})
