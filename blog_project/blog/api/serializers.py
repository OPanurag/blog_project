# blog/api/serializers.py
from rest_framework import serializers
from blog.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published_date', 'author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_date', 'post', 'author']
