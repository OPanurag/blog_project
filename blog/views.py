from django import forms

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template import TemplateDoesNotExist

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from .forms import PostForm
from .models import Post, Comment


@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home', post_id=post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form, 'post': post})


@login_required()
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    try:
        return render(request, 'blog/delete_post.html', {'post': post})
    except TemplateDoesNotExist:
        print("Template delete_post.html not found")
        raise


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
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
        return redirect('post-detail', post_id=post_id)
    return HttpResponse("Invalid request")


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


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', post_id=post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/create_post.html', {'form': form, 'post': post})


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
                user.save()

                # Retrieve the backend and login the user
                backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user, backend=backend)
                return redirect('home')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'blog/signup.html')


def login_view(request):
    if request.method == 'POST':
        print("POST request received")  # Debugging line
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User authenticated")  # Debugging line
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')  # Redirect to home after successful login
            else:
                print("Invalid username or password")  # Debugging line
                messages.error(request, "Invalid username or password.")
        else:
            print("Form is not valid")  # Debugging line
            messages.error(request, "Invalid username or password.")
    else:
        print("GET request received")  # Debugging line
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def logout_view(request):
    auth_logout(request)
    return redirect('home')


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})
