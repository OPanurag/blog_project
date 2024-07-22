from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post, Comment


class PostUpdateDeleteTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpass')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.client.login(username='testuser', password='testpass')

    def test_update_post(self):
        response = self.client.post(reverse('update_post', args=[self.post.id]), {
            'title': 'Updated Title',
            'content': 'Updated Content',
        })
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.content, 'Updated Content')
        self.assertRedirects(response, reverse('post_detail', args=[self.post.id]))

    def test_delete_post(self):
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())
        self.assertRedirects(response, reverse('home'))

    def test_cannot_update_other_users_post(self):
        self.client.logout()
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.post(reverse('update_post', args=[self.post.id]), {
            'title': 'Malicious Update',
            'content': 'Malicious Content',
        })
        self.post.refresh_from_db()
        self.assertNotEqual(self.post.title, 'Malicious Update')
        self.assertNotEqual(self.post.content, 'Malicious Content')
        self.assertEqual(response.status_code, 404)

    def test_cannot_delete_other_users_post(self):
        self.client.logout()
        self.client.login(username='otheruser', password='otherpass')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertTrue(Post.objects.filter(id=self.post.id).exists())
        self.assertEqual(response.status_code, 404)


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
        expected_str = f'{comment.author.username} - {comment.text}'
        self.assertEqual(str(comment), expected_str)


class PostAPITest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        cls.post = Post.objects.create(title='Test Post', content='Test Content', author=cls.user)

    def setUp(self):
        self.client.login(username='testuser', password='testpass')

    def test_get_posts(self):
        response = self.client.get(reverse('post_list'))  # Ensure you have the correct URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_get_single_post(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))  # Ensure you have the correct URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_create_post(self):
        response = self.client.post(reverse('post_list'), {
            'title': 'New Post',
            'content': 'This is a new post',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertContains(response, 'New Post')

    def test_update_post(self):
        response = self.client.put(reverse('post_detail', kwargs={'pk': self.post.pk}), {
            'title': 'Updated Post',
            'content': 'This is the updated content',
            'author': self.user.id
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_delete_post(self):
        response = self.client.delete(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
