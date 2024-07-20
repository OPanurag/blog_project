from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser', password='testpass')
        Post.objects.create(title='Test Post', content='Test Content', author=user)

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Post')


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser', password='testpass')
        post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        Comment.objects.create(post=post, author='Test Author', text='Test Comment')

    def test_text_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.text}'
        self.assertEqual(expected_object_name, 'Test Comment')
