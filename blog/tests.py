from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        user.set_password('testpass')
        user.save()
        Post.objects.create(title='Test Post', content='Test Content', author=user)

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Post')

    def test_string_representation(self):
        post = Post.objects.get(id=1)
        expected_str = 'Test Post'
        self.assertEqual(str(post), expected_str)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        expected_url = f'/posts/{post.id}/'
        self.assertEqual(post.get_absolute_url(), expected_url)

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        user.set_password('testpass')
        user.save()
        post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        Comment.objects.create(post=post, author=user, text='Test Comment')

    def test_text_content(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = f'{comment.text}'
        self.assertEqual(expected_object_name, 'Test Comment')

    def test_string_representation(self):
        comment = Comment.objects.get(id=1)
        expected_str = f'testuser - Test Comment'
        self.assertEqual(str(comment), expected_str)
