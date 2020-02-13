from django.test import TestCase
from django.urls import reverse

from posts.models import Post, Tag

class PostsViewsTest(TestCase):

    def setUp(self):
        Post.objects.create(title='Post 1', content='The post detail 1')
        Post.objects.create(title='Post 2', content='The post detail 2')

    
    def test_root_url_resolve_to_home_page(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    
    def test_home_page_uses_post_list_template(self):
        response = self.client.get(reverse('posts:post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_list.html')

    def test_home_page_returns_list_of_all_posts(self):
        response = self.client.get(reverse('posts:post-list'))

        self.assertEqual(response.status_code, 200)