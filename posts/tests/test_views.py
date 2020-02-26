from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from posts.models import Post, Tag
from posts.forms import PostCreateForm

class PostsViewsTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='Inno')
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
        # self.assertEqual(response.context, '')


    def test_tag_detail_view_uses_correct_template(self):
        tag = Tag.objects.create(name='django')

        response = self.client.get(reverse('posts:tag-detail', kwargs={'slug':tag.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_tag_detail.html')


    def test_post_create_view_with_a_known_user(self):
        self.client.force_login('Inno')
        response = self.client.get(reverse('posts:post-create'))
        self.assertEqual(response.status_code, 200)

    
    def test_post_create_view_with_unknown_user(self):
        response = self.client.get(reverse('posts:post-create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/post/create')